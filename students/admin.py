from django.contrib import admin

from students.models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    ordering = ['id']
    exclude = ['uuid']
    list_per_page = 15


admin.site.register(Student, StudentAdmin)
