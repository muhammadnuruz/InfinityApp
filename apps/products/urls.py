from django.urls import path
from .views import ProductsAPIView, ProductsListAPIView

urlpatterns = [
    path('', ProductsListAPIView.as_view(), name='products-list'),
    path('detail/<int:pk>/', ProductsAPIView.as_view(), name='products-detail')
]
