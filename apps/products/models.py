from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name}"
