from django.contrib import admin

from students.models import Student
from teachers.models import Teacher

# Register your models here.


class StudentsTable(admin.TabularInline):
    """

    A class that represents an inline table of students within the Django admin interface.

    Attributes:
        model (Student): The model that this inline admin table operates on.
        fields (list): A list of fields to be displayed in the table.
        readonly_fields (list): A list of fields that are set to read-only.
        show_change_link (bool): A flag indicating whether to show a link to change the individual student records.
    """

    model = Student
    fields = ['first_name', 'last_name', 'email', 'rating']
    readonly_fields = fields
    show_change_link = True


class TeacherAdmin(admin.ModelAdmin):
    """
    Class representing the admin interface configuration for the Teacher model.

    Attributes:
        exclude (list): List of fields to be excluded from the admin form.
        inlines (list): List of inline related models to be included in the admin form.
        list_per_page (int): Number of items to be displayed per page in the list view.
    """

    exclude = ['uuid']
    inlines = [StudentsTable]
    list_per_page = 10


admin.site.register(Teacher, TeacherAdmin)
