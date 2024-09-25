from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import CreateView
from django.views.generic.edit import ProcessFormView, FormView
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from accounts.forms import AccountCreateForm, AccountUpdateForm, AccountProfileUpdateForm, EmailLoginForm, ContactUsForm
from accounts.signals import send_activation_email
from accounts.tasks import send_contact_email, send_activation_email_task


# Create your views here.


class AccountCreateView(CreateView):
    """
    A view that creates a new user account, with no privileges,
    and sends an activation email.
    """

    model = User
    template_name = "registration.html"
    form_class = AccountCreateForm
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        messages.info(self.request, f'User {self.request.user} (The letter is sent) To continue registration, '
                                    f'follow the link specified in the letter')

        return super().form_valid(form)


class AccountLoginView(LoginView):
    """
    A view that allows a user to login using email and password.
    If the user is not active, an email is sent to the user with an activation link.
    If the user is active, the page is reloaded.
    If the user is inactive, he is redirected to the login page again.
    """

    form_class = EmailLoginForm
    template_name = "login.html"

    def get_redirect_url(self):
        if self.request.GET.get("next"):
            return self.request.GET.get("next")
        return reverse("core:index")

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.info(self.request, f'User {self.request.user} has been successfully logged in')
        return result


class AccountLogoutView(LogoutView):
    """
    A view that allows a user to logout.
    """

    template_name = "logout.html"


class AccountUpdateView(LoginRequiredMixin, ProcessFormView):
    """
    A view that allows a user to update his profile.
    The user must be logged in.
    If the user is active, the page is reloaded.
    If the user is inactive, he is redirected to the login page again.
    """

    def get(self, request, *args, **kwargs):

        user = self.request.user
        profile = self.request.user.profile

        user_form = AccountUpdateForm(instance=user)
        profile_form = AccountProfileUpdateForm(instance=profile)

        return render(
            request,
            "profile.html",
            {
                "user_form": user_form,
                "profile_form": profile_form,
            }
        )

    def post(self, request, *args, **kwargs):

        user = self.request.user
        profile = self.request.user.profile

        user_form = AccountUpdateForm(data=request.POST, instance=user)
        profile_form = AccountProfileUpdateForm(data=request.POST, files=request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse("accounts:profile"))

        return render(
            request,
            "profile.html",
            {
                "user_form": user_form,
                "profile_form": profile_form,
            }
        )


class ContactUsView(LoginRequiredMixin, FormView):
    """
    View to handle contact form submissions.

    This view allows logged-in users to send a message via a contact form.
    Upon successful submission, the form data is processed, and an email is sent asynchronously.
    If an error occurs during email sending, an error message is displayed.
    """

    template_name = "contact_us.html"
    extra_content = {"title": "Send us a message!"}
    success_url = reverse_lazy("core:index")
    form_class = ContactUsForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            try:
                send_contact_email.delay(
                    subject=form.cleaned_data["subject"],
                    message=form.cleaned_data["message"],
                    from_email=request.user.email
                )

                messages.success(request, "Your message has been sent successfully!")
                return self.form_valid(form)

            except Exception as err:
                messages.error(request, f"An error occurred: {err}")
                return self.form_invalid(form)
        else:
            return self.form_invalid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    """
    A view that allows a user to reset his password.
    If the user is active, the page is reloaded.
    If the user is inactive, he is redirected to the login page again.
    If the user does not exist, an error message is displayed.
    """

    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    html_email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'password_reset_subject.txt'


def activate(request, uidb64, token):
    """
    A view that allows a user to activate his account.
    The link must be activated within 48 hours after the account was created.
    If the link is active, the user is redirected to the login page.
    If the link is inactive, an error message is displayed.
    If the user does not exist, an error message is displayed.
    If the user is already active, an error message is displayed.
    """

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        send_activation_email(user, request)
        return redirect('accounts:login')
    else:
        return HttpResponse('Activation link is invalid!')


def resend_confirmation_email(request):
    """
    This view processes a POST request containing an email address. If the email is associated
    with a user account that has not been activated, it will resend the confirmation email to
    that user.
    """

    User = get_user_model()

    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            if not user.is_active:
                current_site = get_current_site(request)
                subject = 'Resend Confirmation Email'
                message = render_to_string('activation_email.html', {
                    'user': user,
                    'domain': current_site.domain if current_site else 'example.com',
                    'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': token_generator.make_token(user),
                })

                send_activation_email_task.delay(subject, message, 'your_email@gmail.com', [user.email])
                messages.success(request, 'Confirmation email sent successfully.')
            else:
                messages.info(request, 'Email is already confirmed.')
        except User.DoesNotExist:
            messages.info(request, 'No account found with this email.')

    return render(request, 'resend_email.html')


def email_open_tracking(request, uidb64):
    """
    Tracks when an email is opened by the user.
    """

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)

        user.email_opened = True
        user.save()

        with open('static/email/open_email_verify.png', 'rb') as f:
            return HttpResponse(f.read(), content_type="image/png")

    except get_user_model().DoesNotExist:
        return HttpResponse(status=404)
