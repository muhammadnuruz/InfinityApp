from apps.students.models import Students
from rest_framework import serializers


class TeachersRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = [
            "id",
            "name",
            "surname",
            "phone_number",
            "created_at"
        ]
