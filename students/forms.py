from django import forms

from students.models import Student


class StudentBaseForms(forms.ModelForm):
    """
    StudentBaseForms is a model form for the Student model.

    This form includes the fields: first_name, last_name, email, birthdate, rating, group, teacher.

    Methods:
        clean_email: Validates the email field to ensure it is not from a blacklisted domain.

        The current blacklist includes:
        - exemple.com
        - exemple.net
    """

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'birthdate', 'rating', 'group', 'teacher']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        blacklist = [
            "exemple.com",
            "exemple.net",
        ]

        domain = email.split('@')[1]

        if domain in blacklist:
            raise forms.ValidationError("This email domain is not allowed")

        return email


class StudentCreateForms(StudentBaseForms):
    """
    Class for creating a student form with specific fields.

    Inherits from:
        StudentBaseForms: Base form class for student-related forms.

    Attributes:
        Meta: Inherits metadata from the base form class and specifies which fields to include from the model.
    """

    class Meta(StudentBaseForms.Meta):

        fields = ['first_name', 'last_name', 'email', 'birthdate']


class StudentEditForms(StudentBaseForms):
    """

         class StudentEditForms(StudentBaseForms):
    class Meta(StudentBaseForms.Meta):

        fields = ['first_name', 'last_name', 'email', 'birthdate', 'rating', 'group', 'teacher']

    A form class for editing student details, extending the base form.

     - StudentEditForms.Meta: Meta class to specify form behavior and options.
     - fields: A list of fields to be included in the form.
        - first_name: First name of the student.
        - last_name: Last name of the student.
        - email: Email address of the student.
        - birthdate: Birthdate of the student.
        - rating: Rating or score of the student.
        - group: Group to which the student belongs.
        - teacher: Teacher assigned to the student.
    """

    class Meta(StudentBaseForms.Meta):

        fields = ['first_name', 'last_name', 'email', 'birthdate', 'rating', 'group', 'teacher']
