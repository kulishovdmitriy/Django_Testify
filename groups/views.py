from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from groups.models import Group
from groups.forms import GroupsCreateForms, GroupsEditForms

# Create your views here.


class GroupsListView(ListView):
    """
    A view that lists groups with optional filtering.

    Attributes
    ----------
    model : type
        The model that this view will operate upon (Group).
    template_name : str
        The template name that this view will render (groups_list.html).
    context_object_name : str
        The context variable name for the object list (groups).
    paginate_by : int
        Number of objects to display per page (20).

    Methods
    -------
    get_queryset():
        Returns a queryset that is optionally filtered based on query parameters.
    """

    model = Group
    template_name = "groups_list.html"
    context_object_name = "groups"
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        request = self.request
        filters = {
            "name": "__icontains",
            "course": "__icontains",
            "start_date": "__icontains",

        }

        for param, lookup in filters.items():
            value = request.GET.get(param)
            if value:
                if lookup:
                    qs = qs.filter(**{f"{param}{lookup}": value})
                else:
                    qs = qs.filter(**{param: value})

        return qs


class GroupsCreateView(LoginRequiredMixin, CreateView):
    """
    A view to handle the creation of new groups.

    Inherits from:
        - LoginRequiredMixin: Ensures that only logged-in users can access the view.
        - CreateView: Provides the functionality to display and process a form for creating a new Group object.

    Attributes:
        model: Specifies the model to be used with this view. In this case, it's the Group model.
        form_class: Specifies the form class to use in this view. This is set to GroupsCreateForms.
        template_name: Specifies the template to be used for rendering the view. This is set to "group_create.html".
        success_url: Specifies the URL to redirect to upon successful form submission. This is set to the URL pattern named "groups:list".
    """

    model = Group
    form_class = GroupsCreateForms
    template_name = "group_create.html"
    success_url = reverse_lazy("groups:list")


class GroupsEditView(LoginRequiredMixin, UpdateView):
    """
    GroupsEditView is a view for editing groups which requires login.
    It uses the UpdateView to allow updates on the Group model.

    Attributes:
    model: Specifies the model to be used, which is Group.
    form_class: Specifies the form to be used, which is GroupsEditForms.
    template_name: Specifies the template to be used, which is "group_edit.html".
    success_url: Specifies the URL to redirect to upon success, which is reverse_lazy("groups:list").
    context_object_name: Specifies the context object name to be used in the template, which is "group".
    pk_url_kwarg: Specifies the keyword argument for the primary key, which is "group_id".

    Methods:
    get_context_data:
        Adds additional context data including students and teachers associated with the group.
    """

    model = Group
    form_class = GroupsEditForms
    template_name = "group_edit.html"
    success_url = reverse_lazy("groups:list")
    context_object_name = "group"
    pk_url_kwarg = "group_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group = self.get_object()
        context['students'] = group.students.all()
        context['teachers'] = group.teachers.all()
        return context


class GroupsDeleteView(LoginRequiredMixin, DeleteView):
    """
    Class-based view to handle deletion of a Group.

    Extends:
        LoginRequiredMixin: Ensures that only authenticated users can access the view.
        DeleteView: Provides the ability to delete a specific instance of a model.

    Attributes:
        model: Specifies the model to be used for the delete operation (Group model).
        template_name: Specifies the template to be used for rendering the confirmation page.
        success_url: URL to redirect to after successful deletion of the Group.
        context_object_name: Name of the context variable to use in the template for the Group object.
        pk_url_kwarg: Name of the URL pattern argument that contains the primary key of the Group to be deleted.
    """

    model = Group
    template_name = "group_confirm_delete.html"
    success_url = reverse_lazy("groups:list")
    context_object_name = "group"
    pk_url_kwarg = "group_id"
