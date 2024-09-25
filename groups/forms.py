from django import forms

from groups.models import Group


class GroupsCreateForms(forms.ModelForm):
    """
        A form for creating and updating Group instances.

        This form inherits from forms.ModelForm and provides fields for the
        Group model, including 'name', 'course', 'start_date', 'head', and 'classrooms'.

        Attributes:
            model: Specifies the model that the form will be based on.
            fields: Lists the fields from the model to be included in the form.
    """

    class Meta:
        model = Group
        fields = ['name', 'course', 'start_date', 'head', 'classrooms']


class GroupsEditForms(GroupsCreateForms):
    pass
