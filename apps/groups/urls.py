from django.urls import path

from apps.groups.views import GroupsListView, GroupsDetailView

urlpatterns = [
    path('', GroupsListView.as_view(), name='books-list'),
    path('<int:pk>/', GroupsDetailView.as_view(), name='books-detail')
]
