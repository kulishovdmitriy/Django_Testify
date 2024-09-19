from django.urls import path

from teachers.api.views import TeacherListView, TeacherListCreateView, TeacherUpdateDeleteView


name_app = ['api_teachers']

urlpatterns = [
    path('teachers', TeacherListView.as_view(), name='teachers_list'),
    path('teachers/create', TeacherListCreateView.as_view(), name='teachers_create'),
    path('teachers/<int:pk>', TeacherUpdateDeleteView.as_view(), name='teachers_detail')
]
