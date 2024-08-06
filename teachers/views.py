from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

from students.utils import format_list
from teachers.models import Teacher
from teachers.forms import TeacherCreateForms

# Create your views here.


def teachers_list(request):
    teachers = Teacher.objects.all()

    params = [
        "first_name",
        "last_name",
        "birthdate",
        "subject",
        "years_of_experience",

    ]
    for param in params:
        value = request.GET.get(param)
        if value:
            teachers = teachers.filter(**{param: value})

    return render(
        request,
        "teachers_list.html",
        {"teachers": format_list(teachers)},
    )


def teacher_create(request):

    if request.method == "GET":
        form_create_teacher = TeacherCreateForms()

    form_create_teacher = TeacherCreateForms(request.POST)
    if form_create_teacher.is_valid():
        form_create_teacher.save()
        return HttpResponseRedirect("/teachers/")

    return render(
        request,
        "teacher_create.html",
        {"form": form_create_teacher}
    )
