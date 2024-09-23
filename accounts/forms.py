from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms

from accounts.models import Profile


User = get_user_model()


class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=254)

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user_model = User

        if email and password:
            try:
                user = user_model.objects.get(email=email)
            except user_model.DoesNotExist:
                raise forms.ValidationError("Invalid email or password")

            if not user.check_password(password):
                raise forms.ValidationError("Invalid email or password")

            if not self.user_cache:
                self.confirm_login_allowed(user)

            self.cleaned_data['username'] = user.username
        return super().clean()


class AccountCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'usable_password' in self.fields:
            del self.fields['usable_password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class AccountUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ["username", "first_name", "last_name", "email"]


class AccountProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "interests"]


class ContactUsForm(forms.Form):
    subject = forms.CharField(max_length=256, initial="Message from University")
    message = forms.CharField(widget=forms.Textarea)
