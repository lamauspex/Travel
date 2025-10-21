from django.contrib import admin
from .models import Category, Location


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'address', 'is_approved', 'created_at')
    list_filter = ('category', 'is_approved', 'created_at')
    search_fields = ('name', 'description', 'address')
    list_editable = ('is_approved',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'category', 'address')
        }),
        ('Геоданные', {
            'fields': ('latitude', 'longitude')
        }),
        ('Медиа', {
            'fields': ('photo',)
        }),
        ('Модерация', {
            'fields': ('is_approved', 'created_at', 'updated_at')
        }),
    )
