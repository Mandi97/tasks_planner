from django.contrib import admin
from . import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'day_name')


@admin.register(models.Planner)
class PlannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created')
    list_filter = ('created', 'title')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
