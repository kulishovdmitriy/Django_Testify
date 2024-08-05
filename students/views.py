from django.shortcuts import render # noqa
from django.http.response import HttpResponse

from students.utils import gen_password, parse_length, format_list
from students.models import Student


# Create your views here.


def hello(request):
    return HttpResponse("Hello from Django!!!")


def get_random(request):
    try:
        length = parse_length(request, 15)
    except Exception as err:
        return HttpResponse(str(err), status_code=400)
    result = gen_password(length)
    return HttpResponse(result)


def students_list(request):
    students = Student.objects.all()

    params = [
        "first_name",
        "last_name",
        "rating",
    ]
    for param in params:
        value = request.GET.get(param)
        if value:
            students = students.filter(**{param: value})

    return HttpResponse(format_list(students))
