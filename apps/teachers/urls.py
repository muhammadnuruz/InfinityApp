from django.urls import path
from .views import TeachersDetailView

urlpatterns = [
    path('detail/<int:pk>/', TeachersDetailView.as_view(), name='teacher-detail')
]
