from django.db import models


class Teachers(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=13, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return f"{self.name}"
