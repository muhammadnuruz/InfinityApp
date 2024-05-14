from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.lessons.serializers import LessonsSerializer, ParticipatedStudentsSerializer
from apps.lessons.models import Lessons, ParticipatedStudents


class LessonsDetail(RetrieveAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        instance = super().get_object()
        instance.is_informed = True
        instance.save()
        return instance

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        attended_students = instance.participated_students.all()
        serializer_data = serializer.data
        serializer_data['attended_students'] = [student.id for student in attended_students]
        return Response(serializer_data)


class UnfinishedLessonsListAPIView(ListAPIView):
    queryset = Lessons.objects.filter(is_finished=True, is_informed=False)
    serializer_class = LessonsSerializer
    permission_classes = [AllowAny]


class StudentStatisticsAPIView(ListAPIView):
    serializer_class = ParticipatedStudentsSerializer

    def get_queryset(self):
        chat_id = self.kwargs.get('chat_id')
        queryset = ParticipatedStudents.objects.filter(student__chat_id=chat_id)
        return queryset


class LessonStudentAPIView(RetrieveAPIView):
    serializer_class = ParticipatedStudentsSerializer

    def retrieve(self, request, *args, **kwargs):
        student_id = self.kwargs.get('student_id')
        lesson_id = self.kwargs.get('lesson_id')
        try:
            queryset = ParticipatedStudents.objects.get(student__id=student_id, lesson__id=lesson_id)
        except ParticipatedStudents.DoesNotExist:
            raise NotFound()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
