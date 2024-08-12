from django.contrib import admin

from students.models import Student
from teachers.models import Teacher

# Register your models here.


class StudentsTable(admin.TabularInline):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'rating']
    readonly_fields = fields
    show_change_link = True


class TeacherAdmin(admin.ModelAdmin):
    exclude = ['uuid']
    inlines = [StudentsTable]


admin.site.register(Teacher, TeacherAdmin)
