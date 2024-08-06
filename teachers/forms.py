from django import forms

from teachers.models import Teacher


class TeacherCreateForms(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'birthdate', 'subject', 'years_of_experience']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        blacklist = [
            "mail.ru",
            "yandex.ru",
        ]

        domain = email.split('@')[1]

        if domain in blacklist:
            raise forms.ValidationError("This email domain is not allowed")

        return email