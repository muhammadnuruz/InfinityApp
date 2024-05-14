from django.contrib import admin
from django.forms import ModelForm

from apps.lessons.models import Lessons, ParticipatedStudents


class ParticipatedStudentsInline(admin.StackedInline):
    model = ParticipatedStudents
    extra = 0


class LessonsAdminForm(ModelForm):
    class Meta:
        model = Lessons
        exclude = ['is_informed']


class LessonsAdmin(admin.ModelAdmin):
    form = LessonsAdminForm
    list_display = ('teacher', 'name', 'group', 'is_finished', 'created_at')
    list_filter = ('teacher', 'name', 'group', 'created_at')
    ordering = ('teacher', 'name', 'group', 'is_finished', 'created_at')
    inlines = [ParticipatedStudentsInline]


class ParticipatedStudentsAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'student', 'evolution', 'infin', 'created_at')
    list_filter = ('lesson', 'student', 'created_at')
    ordering = ('lesson', 'student', 'created_at')


# admin.site.register(ParticipatedStudents, ParticipatedStudentsAdmin)
admin.site.register(Lessons, LessonsAdmin)
