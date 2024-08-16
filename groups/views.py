from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from groups.models import Group
from groups.forms import GroupsCreateForms, GroupsEditForms

# Create your views here.


class GroupsListView(ListView):

    model = Group
    template_name = "groups_list.html"
    context_object_name = "groups"

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

    model = Group
    form_class = GroupsCreateForms
    template_name = "group_create.html"
    success_url = reverse_lazy("groups:list")


class GroupsEditView(LoginRequiredMixin, UpdateView):

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

    model = Group
    template_name = "group_confirm_delete.html"
    success_url = reverse_lazy("groups:list")
    context_object_name = "group"
    pk_url_kwarg = "group_id"
