from django.urls import path

from groups.api.views import GroupListView, GroupListCreateView, GroupUpdateDeleteView


name_app = ['api_groups']

urlpatterns = [
    path('groups', GroupListView.as_view(), name='groups_list'),
    path('groups/create', GroupListCreateView.as_view(), name='groups_create'),
    path('groups/<int:pk>', GroupUpdateDeleteView.as_view(), name='groups_detail')
]
