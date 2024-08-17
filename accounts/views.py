from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import AccountCreateForm, AccountUpdateForm


# Create your views here.

class AccountCreateView(CreateView):

    model = User
    template_name = "registration.html"
    form_class = AccountCreateForm
    success_url = reverse_lazy("core:index")


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


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "profile.html"
    form_class = AccountUpdateForm
    success_url = reverse_lazy("core:index")

    def get_object(self, queryset=None):
        return self.request.user
