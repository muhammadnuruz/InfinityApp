from django.contrib import admin

from .models import Teachers


class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone_number', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'surname', 'phone_number')
    ordering = ('created_at',)


admin.site.register(Teachers, TeachersAdmin)
