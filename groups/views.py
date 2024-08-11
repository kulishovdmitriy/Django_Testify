from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from groups.models import Group
from groups.forms import GroupsCreateForms
# Create your views here.


def get_groups(request):
    groups = Group.objects.all()

    params = [
        "name",
        "course",
        "start_date",

    ]
    for param in params:
        value = request.GET.get(param)
        if value:
            groups = groups.filter(**{param: value})

    return render(
        request,
        "groups_list.html",
        {
            "groups": groups,
        }
    )


def create_group(request):

    if request.method == "GET":
        form = GroupsCreateForms()

    form_create_group = GroupsCreateForms(request.POST)

    if form_create_group.is_valid():

        form_create_group.save()
        return HttpResponseRedirect(reverse("groups:list"))

    return render(
        request,
        "group_create.html",
        {
            "form": form,
        }
    )


def edit_group(request, group_id):

    group = get_object_or_404(Group, id=group_id)

    if request.method == "GET":
        form = GroupsCreateForms(instance=group)

    elif request.method == "POST":
        form = GroupsCreateForms(request.POST, instance=group)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("groups:list"))

    return render(
        request,
        "group_edit.html",
        {
            "form": form,
            "group": group,
            "students": group.students.all(),
            "teachers": group.teachers.all(),
        }
    )


def delete_group(request, group_id):

    group = get_object_or_404(Group, id=group_id)

    group.delete()

    return HttpResponseRedirect(reverse("groups:list"))
