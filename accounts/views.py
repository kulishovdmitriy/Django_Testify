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
        return reverse("core:index")


class AccountLogoutView(LogoutView):

    template_name = "logout.html"


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "profile.html"
    form_class = AccountUpdateForm
    success_url = reverse_lazy("core:index")

    def get_object(self, queryset=None):
        return self.request.user
