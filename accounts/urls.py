"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:

    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Examples:
Function views

    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views

    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from accounts.views import (
    AccountCreateView,
    AccountLoginView,
    AccountLogoutView,
    AccountUpdateView,
    ResetPasswordView,
    ContactUsView,
    activate,
    resend_confirmation_email,
    email_open_tracking,
)


app_name = "accounts"

urlpatterns = [

    path('registration/', AccountCreateView.as_view(), name='registration'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('profile/', AccountUpdateView.as_view(), name='profile'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('contact_us/', ContactUsView.as_view(), name='contact_us'),
    path('resend_email/', resend_confirmation_email, name='resend_email'),
    path('email_open/<uidb64>/', email_open_tracking, name='email_open'),

    path('password/', ResetPasswordView.as_view(), name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',
                                          success_url='/accounts/reset-password/complete/'),
         name='password_reset_confirm'),
    path('reset-password/complete/',
         PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),

]
