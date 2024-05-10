from django.urls import path
from .views import StudentsDetailView, StudentsChatIdDetailView, StudentsPhoneNumberDetailView, StudentsUpdateView

urlpatterns = [
    path('detail/<int:pk>/', StudentsDetailView.as_view(), name='student-detail'),
    path('update/<int:pk>/', StudentsUpdateView.as_view(), name='student-update'),
    path('chat_id/<str:chat_id>/', StudentsChatIdDetailView.as_view(), name='student-chat_id'),
    path('phone_number/<str:phone_number>/', StudentsPhoneNumberDetailView.as_view(), name='student-phone_number')
]
