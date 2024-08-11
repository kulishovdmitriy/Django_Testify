from django.contrib import admin

from teachers.models import Teacher

# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    exclude = ['uuid']


admin.site.register(Teacher, TeacherAdmin)
