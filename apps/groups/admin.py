from django.contrib import admin
from apps.groups.models import Groups


class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


admin.site.register(Groups, GroupsAdmin)
