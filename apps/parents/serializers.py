from apps.parents.models import Parents
from rest_framework import serializers


class ParentsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = [
            "id",
            "father_name",
            "mother_name",
            "father_surname",
            "mother_surname",
            "father_phone_number",
            "mother_phone_number",
            "father_birth_date",
            "mother_birth_date",
            "created_at"
        ]
