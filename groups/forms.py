from django import forms

from groups.models import Group


class GroupsCreateForms(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'course', 'start_date', 'head', 'classrooms']
