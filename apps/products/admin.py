from django.contrib import admin

from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('created_at',)
    search_fields = ('name',)
    ordering = ('price', 'name', 'created_at')


admin.site.register(Products, ProductsAdmin)
