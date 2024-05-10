from django.db import models

from apps.groups.models import Groups
from apps.students.models import Students
from apps.teachers.models import Teachers


class Lessons(models.Model):
    SPEAKING = 'speaking'
    VOCABULARY = 'vocabulary'
    GRAMMAR = 'grammar'

    NAME_CHOICES = [
        (SPEAKING, 'Speaking'),
        (VOCABULARY, 'Vocabulary'),
        (GRAMMAR, 'Grammar'),
    ]
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(choices=NAME_CHOICES, max_length=20)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name='lessons')
    is_finished = models.BooleanField(default=False)
    is_informed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def __str__(self):
        return f"{self.teacher}-{self.group}"


class ParticipatedStudents(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='participated_students')
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='participated_students')
    evaluation = models.IntegerField(default=0)
    is_do_homework = models.BooleanField(default=False)
    infin = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.student}-{self.lesson}"

    def save(self, *args, **kwargs):
        self.student.infin += self.infin
        self.student.save()
        super().save(*args, **kwargs)


class AbsentStudents(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='absent_students')
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='absent_students')
    is_reason = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Absent Student"
        verbose_name_plural = "Absent Students"

    def __str__(self):
        return f"{self.student}-{self.lesson}"
