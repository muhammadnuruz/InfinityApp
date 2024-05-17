from django.urls import path

from apps.lessons.views import LessonsDetail, UnfinishedLessonsListAPIView, StudentStatisticsAPIView, \
    LessonStudentAPIView, MonthStatisticView

urlpatterns = [
    path('<int:pk>/', LessonsDetail.as_view(), name='lesson-detail'),
    path('unfinished_filter/', UnfinishedLessonsListAPIView.as_view(), name='lesson-filter'),
    path('statistic_filter/<str:chat_id>/', StudentStatisticsAPIView.as_view(), name='student-statistics'),
    path('lesson_student/<str:student_id>/<int:lesson_id>/', LessonStudentAPIView.as_view(), name='lesson-student'),
    path('month_statistic/<int:group_id>/', MonthStatisticView.as_view(), name='month-statistics'),
]
