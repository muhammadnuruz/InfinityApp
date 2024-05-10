from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from apps.products.models import Products
from apps.products.serializers import ProductsRetrieveSerializer


class ProductsListAPIView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsRetrieveSerializer
    permission_classes = [AllowAny]


class ProductsAPIView(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsRetrieveSerializer
    permission_classes = [AllowAny]
