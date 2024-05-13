from django.db import models

from apps.students.models import Students


class Parents(models.Model):
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_surname = models.CharField(max_length=100)
    mother_surname = models.CharField(max_length=100)
    father_phone_number = models.CharField(max_length=13, unique=True)
    mother_phone_number = models.CharField(max_length=13, unique=True)
    # password = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Parent"
        verbose_name_plural = "Parents"

    def __str__(self):
        return f"{self.father_name}-{self.mother_name}"

    def get_children(self):
        return Students.objects.filter(parent=self)
