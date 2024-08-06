from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

from students.forms import StudentCreateForms
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

    return render(
        request,
        "students_list.html",
        {"students": format_list(students)},
    )


def students_create(request):

    if request.method == "GET":
        form = StudentCreateForms()

    form_create_student = StudentCreateForms(request.POST)

    if form_create_student.is_valid():

        form_create_student.save()
        return HttpResponseRedirect("/students/")

    return render(
        request,
        "students_create.html",
        {"form": form_create_student}
    )
