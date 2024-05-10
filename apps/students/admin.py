from django.contrib import admin
from django.forms import ModelForm

from .models import Students


class StudentsAdminForm(ModelForm):
    class Meta:
        model = Students
        exclude = ['step']


class StudentsAdmin(admin.ModelAdmin):
    form = StudentsAdminForm
    list_display = (
        'name', 'surname', 'phone_number', 'infin', 'group', 'parent', 'chat_id', 'created_at')
    list_filter = ('group', 'parent', 'created_at')
    search_fields = ('name', 'surname', 'phone_number', 'chat_id')


admin.site.register(Students, StudentsAdmin)
