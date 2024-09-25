from django.http.response import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from teachers.models import Teacher
from teachers.forms import TeacherCreateForms, TeacherEditForms

# Create your views here.


class TeachersListView(ListView):
    """

    A view that lists Teacher objects with optional filtering.

    Extends:
        ListView: A generic ListView that provides a list of objects.

    Attributes:
        model (Model): Specifies the model to be used (Teacher).
        template_name (str): Specifies the template to be used for rendering the list.
        context_object_name (str): The context variable name to be used in the template (teachers).
        paginate_by (int): Number of items to be displayed per page (20).
    """

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
    """
    class TeachersCreateView:
        A view to handle the creation of new Teacher objects.
        This class-based view ensures that only authenticated users can access it,
        and it leverages Django's CreateView to provide form handling and validation for creating Teacher instances.

        model: Specifies the model that the view will operate on, which is the Teacher model.
        form_class: Defines the form class to be used for creating a new Teacher.
        template_name: Points to the template that should be rendered when the view is accessed.
        success_url: Determines the URL to redirect to upon successful form submission.
    """

    model = Teacher
    form_class = TeacherCreateForms
    template_name = "teacher_create.html"
    success_url = reverse_lazy("teachers:list")


class TeachersEditView(LoginRequiredMixin, UpdateView):
    """
    TeachersEditView is a Django view that enables editing a teacher's profile.

    This view requires user authentication and is accessible to logged-in users only.
    It uses the UpdateView class to facilitate editing a teacher's information.

    Attributes:
        model: Specifies the Django model to use (Teacher).
        form_class: Indicates the form class to use for editing (TeacherEditForms).
        template_name: The template to render for this view ("teacher_edit.html").
        success_url: The URL to redirect to upon successful form submission, resolves to "teachers:list".
        context_object_name: The name of the context object used in the template ("teacher").
        pk_url_kwarg: The URL keyword argument that contains the primary key value ("uuid").

    Methods:
        get_object(queryset=None):
            Retrieves the teacher object based on the UUID provided in the URL parameters.
            Args:
                queryset: Optional queryset to filter the model objects.
            Returns:
                The teacher instance matching the UUID.

        get_context_data(**kwargs):
            Adds additional context data to be passed to the template.
            Args:
                **kwargs: Additional keyword arguments.
            Returns:
                The context dictionary with an added key "students" containing all students related to the teacher.
    """

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
    """
        TeachersDeleteView is a Django class-based view that handles the deletion of Teacher objects.

        Attributes:
        model (Model): Specifies the model to be used, which is the Teacher model.
        template_name (str): Path to the template used to confirm the deletion.
        success_url (str): URL to redirect after successful deletion, using reverse_lazy to avoid ImportErrors.
        context_object_name (str): Name of the context variable that will be used in the template.
        pk_url_kwarg (str): Keyword argument used to identify the object to be deleted, specified as 'uuid'.

        Methods:
        get_object(self, queryset=None):
            Retrieves the Teacher object based on the 'uuid' provided in the URL keyword arguments.
            If the 'uuid' is not found, raises an Http404 exception.

        Raises:
        Http404: If the 'uuid' parameter is not provided or if the Teacher object with the given 'uuid' is not found.
    """

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
