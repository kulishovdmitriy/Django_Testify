from django import forms

from teachers.models import Teacher


class TeacherCreateForms(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'birthdate', 'subject', 'years_of_experience']
