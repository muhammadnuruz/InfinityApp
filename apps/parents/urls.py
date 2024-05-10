from django.urls import path
from .views import ParentsDetailView

urlpatterns = [
    path('detail/<int:pk>/', ParentsDetailView.as_view(), name='parents-detail')
]
