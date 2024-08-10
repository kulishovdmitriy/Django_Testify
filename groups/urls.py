"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from groups.views import get_groups, create_group, edit_group, delete_group

app_name = "groups"

urlpatterns = [
    path('', get_groups, name='list'),
    path('create/', create_group, name='create'),
    path('edit/<int:group_id>', edit_group, name='edit'),
    path('delete/<int:group_id>', delete_group, name='delete')
]
