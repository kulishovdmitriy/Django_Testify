from django.shortcuts import render, reverse, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect

from students.forms import StudentCreateForms
from students.models import Student

# Create your views here.


def hello(request):
    return HttpResponse("Hello from Django!!!")


def get_students(request):
    students = Student.objects.all()

    params = [
        "first_name",
        "last_name",
        "email",
        "rating",
        "birthdate",
    ]
    for param in params:
        value = request.GET.get(param)
        if value:
            students = students.filter(**{param: value})

    return render(
        request,
        "students_list.html",
        {
            "students": students,
        }
    )


def create_student(request):

    if request.method == "GET":
        form = StudentCreateForms()

    form_create_student = StudentCreateForms(request.POST)

    if form_create_student.is_valid():

        form_create_student.save()
        return HttpResponseRedirect(reverse("students:list"))

    return render(
        request,
        "students_create.html",
        {
            "form": form,
        }
    )


def edit_student(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == "GET":
        form = StudentCreateForms(instance=student)

    elif request.method == "POST":
        form = StudentCreateForms(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("students:list"))

    return render(
        request,
        "students_edit.html",
        {
            "form": form,
            "student": student,
        }
    )


def delete_student(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    student.delete()

    return HttpResponseRedirect(reverse("students:list"))
