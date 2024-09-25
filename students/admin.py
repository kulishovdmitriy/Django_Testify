from django.contrib import admin

from students.models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    """

    Class for customizing the admin interface for the Student model.

    Attributes:
        ordering (list): Defines the default ordering for the change list.
        exclude (list): A list of fields to exclude from the form.
        list_per_page (int): Number of objects to display per page of the change list.
    """

    ordering = ['id']
    exclude = ['uuid']
    list_per_page = 15


admin.site.register(Student, StudentAdmin)
