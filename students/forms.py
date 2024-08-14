from django import forms

from students.models import Student


class StudentBaseForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'birthdate', 'rating', 'group', 'teacher']

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


class StudentCreateForms(StudentBaseForms):
    class Meta(StudentBaseForms.Meta):

        fields = ['first_name', 'last_name', 'email', 'birthdate']


class StudentEditForms(StudentBaseForms):
    class Meta(StudentBaseForms.Meta):

        fields = ['first_name', 'last_name', 'email', 'birthdate', 'rating', 'group', 'teacher']
