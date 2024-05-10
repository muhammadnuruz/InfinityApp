from django.urls import path

from apps.lessons.views import LessonsDetail, UnfinishedLessonsListAPIView, StudentStatisticsAPIView, \
    LessonStudentAPIView

urlpatterns = [
    path('<int:pk>/', LessonsDetail.as_view(), name='lesson-detail'),
    path('unfinished_filter/', UnfinishedLessonsListAPIView.as_view(), name='lesson-filter'),
    path('statistic_filter/<str:chat_id>/', StudentStatisticsAPIView.as_view(), name='student-statistics'),
    path('lesson_student/<str:student_id>/<int:lesson_id>/', LessonStudentAPIView.as_view(), name='lesson-student')
]
