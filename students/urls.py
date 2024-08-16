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

from students.views import StudentsListView, StudentsCreateView, StudentsEditView, StudentsDeleteView

app_name = "students"

urlpatterns = [
    path('', StudentsListView.as_view(), name='list'),
    path('create/', StudentsCreateView.as_view(), name='create'),
    path('edit/<uuid:uuid>', StudentsEditView.as_view(), name='edit'),
    path('delete/<uuid:uuid>', StudentsDeleteView.as_view(), name='delete')

]
