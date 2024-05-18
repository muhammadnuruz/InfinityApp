from apps.lessons.models import Lessons, ParticipatedStudents
from rest_framework import serializers


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ['id', 'teacher', 'name', 'group', 'is_finished', 'is_informed', 'created_at']


class ParticipatedStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipatedStudents
        fields = ['id', 'student', 'evaluation', 'infin', 'created_at']


class AggregatedParticipatedStudentSerializer(serializers.Serializer):
    student_name = serializers.CharField(max_length=100)
    student_surname = serializers.CharField(max_length=100)
    student_id = serializers.IntegerField()
    average_evaluation = serializers.IntegerField()
