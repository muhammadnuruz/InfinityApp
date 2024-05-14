from django.db import models

from apps.students.models import Students


class Groups(models.Model):
    name = models.CharField(max_length=255, unique=True)
    group_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return f"{self.name}"

    def get_students(self):
        return Students.objects.filter(group=self)
