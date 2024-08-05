from django.shortcuts import render # noqa
from django.http.response import HttpResponse

from students.utils import format_list
from teachers.models import Teacher

# Create your views here.


def teachers_list(request):
    students = Teacher.objects.all()

    params = [
        "first_name",
        "last_name",
        "subject",
        "years_of_experience",

    ]
    for param in params:
        value = request.GET.get(param)
        if value:
            students = students.filter(**{param: value})

    return HttpResponse(format_list(students))
