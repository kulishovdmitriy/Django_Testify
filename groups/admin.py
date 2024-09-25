from django.contrib import admin

from groups.models import ClassRoom, Group
from students.models import Student


# Register your models here.


class StudentTable(admin.TabularInline):
    """
    class StudentTable(admin.TabularInline):
        Represents a tabular inline form for the Student model in the Django admin interface.

        Attributes:
            model: The model class associated with this inline form, in this case, Student.
            fields: A list of field names to be displayed in the inline form.
            readonly_fields: A list of fields that should be read-only in the inline form.
            show_change_link: A boolean indicating whether to show a link to the change form for each inline instance.
    """

    model = Student
    fields = ['first_name', 'last_name', 'email', 'rating']
    readonly_fields = fields
    show_change_link = True


class GroupAdmin(admin.ModelAdmin):
    """
    Represents the Django admin configuration for the Group model.

    Attributes:

        inlines: List of inline model forms to be displayed on the admin page for the Group model.
    """

    # list_display = ['name', 'course', 'head']
    # fields = ['name', 'course', 'head', 'classrooms']
    inlines = [StudentTable]


admin.site.register(ClassRoom)

admin.site.register(Group, GroupAdmin)
