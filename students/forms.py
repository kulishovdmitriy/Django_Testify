from django import forms

from students.models import Student


class StudentCreateForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'birthdate', 'rating']
