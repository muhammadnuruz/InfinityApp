from apps.lessons.models import Lessons, ParticipatedStudents
from rest_framework import serializers


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ['id', 'teacher', 'name', 'group', 'is_finished', 'is_informed', 'created_at']


class ParticipatedStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipatedStudents
        fields = ['id', 'student', 'evaluation', 'is_do_homework', 'infin']
