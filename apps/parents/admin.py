from django.contrib import admin

from .models import Parents


class ParentsAdmin(admin.ModelAdmin):
    list_display = (
        'father_name', 'mother_name', 'father_phone_number', 'mother_phone_number', 'created_at')
    list_filter = ('created_at',)
    search_fields = (
        'father_name', 'mother_name', 'father_surname', 'mother_surname', 'father_phone_number', 'mother_phone_number',
        'phone_number')
    ordering = ('created_at',)


admin.site.register(Parents, ParentsAdmin)
