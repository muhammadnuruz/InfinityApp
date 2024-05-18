from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Avg, F
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from apps.lessons.serializers import LessonsSerializer, ParticipatedStudentsSerializer, \
    AggregatedParticipatedStudentSerializer
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


class MonthStatisticView(ListAPIView):
    serializer_class = AggregatedParticipatedStudentSerializer

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        now = datetime.now()
        first_day_of_current_month = make_aware(datetime(now.year, now.month, 1))
        last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)
        first_day_of_previous_month = make_aware(
            datetime(last_day_of_previous_month.year, last_day_of_previous_month.month, 1))
        lessons = Lessons.objects.filter(group_id=group_id, created_at__gte=first_day_of_previous_month,
                                         created_at__lt=first_day_of_current_month)
        return ParticipatedStudents.objects.filter(lesson__in=lessons).values(
            'student_id',
            student_name=F('student__name'),   # Rename field to match serializer
            student_surname=F('student__surname') # Rename field to match serializer
        ).annotate(
            average_evaluation=Avg('evaluation')
        ).order_by('student_id')
