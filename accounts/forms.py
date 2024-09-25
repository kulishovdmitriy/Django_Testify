from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms

from accounts.models import Profile


User = get_user_model()


class EmailLoginForm(AuthenticationForm):
    """

    class EmailLoginForm(AuthenticationForm):
        A custom authentication form that uses an email field
        for user login instead of the default username field.

    Attributes:
        username (forms.EmailField): A form field for the email
        of the user with a maximum length constraint of 254 characters.

    Methods:
        clean(): Validates the email and password provided by the user.
            Raises a ValidationError if the login credentials are invalid
            or if the user is not allowed to log in.
    """

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
    """
    A custom user creation form that uses an email field
    for user registration instead of the default username field.
    """

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
    """
    A custom user update form that uses an email field
    for user registration instead of the default username field.
    """

    class Meta(UserChangeForm.Meta):
        fields = ["username", "first_name", "last_name", "email"]


class AccountProfileUpdateForm(ModelForm):
    """
        A form for updating user profile information, specifically the profile
        image and interests. Inherits from Django's ModelForm.

        Attributes:
            model: Specifies the model that this form will interact with. In this
            case, it is the Profile model.
            fields: Lists the fields from the Profile model that will be included
            in the form. These are 'image' and 'interests'.
    """

    class Meta:
        model = Profile
        fields = ["image", "interests"]


class ContactUsForm(forms.Form):
    """
    ContactUsForm is a Django form used to gather information from users who
    wish to contact a university.

    Attributes:
        subject (CharField): A text field for users to specify the subject
            of their message, with a default initial value of
            "Message from University" and a maximum length of 256 characters.
        message (CharField): A text area field for users to provide the
            content of their message.
    """

    subject = forms.CharField(max_length=256, initial="Message from University")
    message = forms.CharField(widget=forms.Textarea)
