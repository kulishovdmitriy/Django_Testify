from django.http.response import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from students.forms import StudentCreateForms, StudentEditForms
from students.models import Student

# Create your views here.


class StudentsListView(ListView):

    model = Student
    template_name = "students_list.html"
    context_object_name = "students"

    def get_queryset(self):
        qs = super().get_queryset()
        request = self.request
        params = {
            "first_name": "__icontains",
            "last_name": "__icontains",
            "email": "__icontains",
            "rating": "",
            "birthdate": "",
        }
        for param, lookup in params.items():
            value = request.GET.get(param)
            if value:
                if lookup:
                    qs = qs.filter(**{f"{param}{lookup}": value})
                else:
                    qs = qs.filter(**{param: value})

        return qs


class StudentsCreateView(LoginRequiredMixin, CreateView):

    model = Student
    form_class = StudentCreateForms
    template_name = "students_create.html"
    success_url = reverse_lazy("students:list")


class StudentsEditView(LoginRequiredMixin, UpdateView):

    model = Student
    form_class = StudentEditForms
    template_name = "students_edit.html"
    success_url = reverse_lazy("students:list")
    context_object_name = "student"
    pk_url_kwarg = "uuid"

    def get_object(self, queryset=None):
        uuid = self.kwargs.get("uuid")
        return self.get_queryset().get(uuid=uuid)


class StudentsDeleteView(LoginRequiredMixin, DeleteView):

    model = Student
    template_name = "student_confirm_delete.html"
    success_url = reverse_lazy("students:list")
    context_object_name = "student"
    pk_url_kwarg = "uuid"

    def get_object(self, queryset=None):
        uuid = self.kwargs.get(self.pk_url_kwarg)
        if not uuid:
            raise Http404("Student not found")
        return self.get_queryset().get(uuid=uuid)
