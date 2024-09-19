from django.urls import path

from students.api.views import StudentListView, StudentListCreateView, StudentUpdateDeleteView


app_name = 'api_students'

urlpatterns = [
    path('students', StudentListView.as_view(), name='students_list'),
    path('students/create', StudentListCreateView.as_view(), name='students_create'),
    path('students/<int:pk>', StudentUpdateDeleteView.as_view(), name='student_detail')
]
