from django.contrib import admin

from groups.models import ClassRoom, Group
from students.models import Student


# Register your models here.


class StudentTable(admin.TabularInline):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'rating']
    readonly_fields = fields
    show_change_link = True


class GroupAdmin(admin.ModelAdmin):
    # list_display = ['name', 'course', 'head']
    # fields = ['name', 'course', 'head', 'classrooms']
    inlines = [StudentTable]


admin.site.register(ClassRoom)
admin.site.register(Group, GroupAdmin)
