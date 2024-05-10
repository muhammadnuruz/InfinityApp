from apps.products.models import Products
from rest_framework import serializers


class ProductsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "price",
            "created_at"
        ]
