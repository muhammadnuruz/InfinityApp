from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=13, unique=True)
    password = models.CharField(max_length=6)
    chat_id = models.CharField(max_length=50, default=0)
    infin = models.IntegerField(default=0)
    # purchased_items
    parent = models.ForeignKey("parents.Parents", on_delete=models.CASCADE, related_name='students', null=True)
    group = models.ForeignKey("groups.Groups", on_delete=models.CASCADE, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    step = models.JSONField(default=dict)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.name}-{self.surname}"
