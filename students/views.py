from django.http.response import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from students.forms import StudentCreateForms, StudentEditForms
from students.models import Student

# Create your views here.


class StudentsListView(ListView):
    """
    A subclass of ListView for displaying a paginated list of students with optional filtering based on query parameters.

    Attributes:
        model: The model that this view will operate upon, which is Student.
        template_name: The template to use when rendering the list of students.
        context_object_name: The context variable to use when rendering the list in the template.
        paginate_by: The number of students to display per page.

    Methods:
        get_queryset: Returns a queryset of students, optionally filtered based on query parameters present in the request.
            The following parameters are checked:
            - first_name: Filtered using case-insensitive matching.
            - last_name: Filtered using case-insensitive matching.
            - email: Filtered using case-insensitive matching.
            - rating: Filtered using exact match.
            - birthdate: Filtered using exact match.
    """

    model = Student
    template_name = "students_list.html"
    context_object_name = "students"
    paginate_by = 20

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
    """

    StudentsCreateView is a class-based view for handling the creation of new students. It utilizes the `LoginRequiredMixin` to ensure that only authenticated users can access this view and `CreateView` to provide the necessary functionality for creating new records.

    Attributes:
        model: Specifies the model that is associated with this view, in this case, `Student`.
        form_class: Defines the form that will be used to create a new student instance, here it's `StudentCreateForms`.
        template_name: Indicates the template to be used when rendering this view, which is "students_create.html".
        success_url: Specifies the URL to which the user will be redirected upon successful creation of a new student, which is the "students:list" view.
    """

    model = Student
    form_class = StudentCreateForms
    template_name = "students_create.html"
    success_url = reverse_lazy("students:list")


class StudentsEditView(LoginRequiredMixin, UpdateView):
    """
    StudentsEditView is a CBV (Class-Based View) for editing a Student object.
    Inherits from:
    - LoginRequiredMixin: Ensures that the user is logged in to access this view.
    - UpdateView: Provides the ability to update a specific object.

    Attributes:
    - model: Specifies the model that this view will operate on, which is the Student model.
    - form_class: Defines the form used to edit the Student object, which is StudentEditForms.
    - template_name: Specifies the template to render for this view, which is "students_edit.html".
    - success_url: Determines the URL to redirect to when the form is successfully submitted, defined using reverse_lazy with the pattern named "students:list".
    - context_object_name: Sets the context variable name to "student".
    - pk_url_kwarg: Specifies the name of the keyword argument that will be used to retrieve the object's primary key, using "uuid".

    Methods:

    get_object(self, queryset=None):
        Retrieves a Student object using the UUID provided in the URL.

        Args:
        - queryset: An optional QuerySet that can be passed in. If not provided, the default queryset will be used.

        Returns:
        - A Student object with the matching UUID obtained from the URL.
    """

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
    """
        StudentsDeleteView class handles the functionality to delete a student.

        Inherits from:
            LoginRequiredMixin: Ensures the user is logged in to access this view.
            DeleteView: Provides the delete functionality for a specific object.

        Attributes:
            model: Specifies the model to be used, which is Student.
            template_name: The template to render for confirming the deletion.
            success_url: URL to redirect after a successful delete operation.
            context_object_name: Name of the context variable to use in the template.
            pk_url_kwarg: Keyword argument used to look up the Student by its unique identifier (uuid).

        Methods:
            get_object(self, queryset=None):
                Retrieves the Student object based on the uuid provided in the URL kwargs.
                Raises Http404 if the uuid is not found or does not exist.
    """

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
