from apps.students.models import Students
from rest_framework import serializers


class StudentsRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = [
            "id",
            "name",
            "surname",
            "phone_number",
            "infin",
            "group",
            "parent",
            'chat_id',
            'password',
            "created_at",
        ]


class StudentsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = [
            "infin",
            "chat_id"
        ]
