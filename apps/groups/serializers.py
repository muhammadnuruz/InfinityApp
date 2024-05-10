from apps.groups.models import Groups
from rest_framework import serializers


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['id', 'name']


class GroupsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['id', 'name', 'created_at']
