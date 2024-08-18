from django.http.response import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from teachers.models import Teacher
from teachers.forms import TeacherCreateForms, TeacherEditForms

# Create your views here.


class TeachersListView(ListView):

    model = Teacher
    template_name = "teachers_list.html"
    context_object_name = "teachers"
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        request = self.request
        filters = {
            "first_name": "__icontains",
            "last_name": "__icontains",
            "email": "__icontains",
            "subject": "__icontains",
            "birthdate": None,
            "years_of_experience": "__icontains",
        }

        for param, lookup in filters.items():
            value = request.GET.get(param)
            if value:
                if lookup:
                    qs = qs.filter(**{f"{param}{lookup}": value})
                else:
                    qs = qs.filter(**{param: value})

        return qs


class TeachersCreateView(LoginRequiredMixin, CreateView):

    model = Teacher
    form_class = TeacherCreateForms
    template_name = "teacher_create.html"
    success_url = reverse_lazy("teachers:list")


class TeachersEditView(LoginRequiredMixin, UpdateView):

    model = Teacher
    form_class = TeacherEditForms
    template_name = "teacher_edit.html"
    success_url = reverse_lazy("teachers:list")
    context_object_name = "teacher"
    pk_url_kwarg = "uuid"

    def get_object(self, queryset=None):
        uuid = self.kwargs.get("uuid")
        return self.get_queryset().get(uuid=uuid)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.get_object()
        context['students'] = teacher.students.all()
        return context


class TeachersDeleteView(LoginRequiredMixin, DeleteView):

    model = Teacher
    template_name = "teacher_confirm_delete.html"
    success_url = reverse_lazy("teachers:list")
    context_object_name = "teacher"
    pk_url_kwarg = "uuid"

    def get_object(self, queryset=None):
        uuid = self.kwargs.get(self.pk_url_kwarg)
        if not uuid:
            raise Http404("Student not found")
        return self.get_queryset().get(uuid=uuid)
