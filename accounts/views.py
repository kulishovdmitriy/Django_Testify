from django.contrib import messages
from django.views.generic.edit import ProcessFormView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http.response import HttpResponseRedirect

from accounts.forms import AccountCreateForm, AccountUpdateForm, AccountProfileUpdateForm

from accounts.models import Profile # noqa

# Create your views here.


class AccountCreateView(CreateView):

    model = User
    template_name = "registration.html"
    form_class = AccountCreateForm
    success_url = reverse_lazy("accounts:login")


class AccountLoginView(LoginView):

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

    template_name = "logout.html"


class AccountUpdateView(LoginRequiredMixin, ProcessFormView):

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
