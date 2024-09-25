from django import forms

from teachers.models import Teacher


class TeacherBaseForms(forms.ModelForm):
    """
     class TeacherBaseForms(forms.ModelForm):
     A form for creating and updating Teacher instances. Each field corresponds to a Teacher model attribute.

     class Meta:
         model = Teacher
         fields = ['first_name', 'last_name', 'email', 'birthdate', 'subject', 'years_of_experience', 'group']
         Specifies the model and fields to be used in the form.

     def clean_email(self):
         Validates the email address. Ensures that the email domain is not in the blacklist.
         Raise:
             forms.ValidationError: If the email domain is in the blacklist.
         Returns:
             str: The validated email address.
    """

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'birthdate', 'subject', 'years_of_experience', 'group']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        blacklist = [
            "example.com",
            "example.net",
        ]

        domain = email.split('@')[1]

        if domain in blacklist:
            raise forms.ValidationError("This email domain is not allowed")

        return email


class TeacherCreateForms(TeacherBaseForms):
    """
    class TeacherCreateForms(TeacherBaseForms):
        Meta class inheriting from TeacherBaseForms.Meta.

        Meta: Configuration for the TeacherCreateForms.
    """

    class Meta(TeacherBaseForms.Meta):
        pass


class TeacherEditForms(TeacherBaseForms):
    """
    class TeacherEditForms(TeacherBaseForms):
    This form class is used for handling teacher edit forms,
    inheriting the attributes and methods from TeacherBaseForms.

    class Meta(TeacherBaseForms.Meta):
    Metadata class to specify the model and fields for the form,
    inheriting the metadata properties from TeacherBaseForms.Meta.
    """

    class Meta(TeacherBaseForms.Meta):
        pass
