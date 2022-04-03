from django.contrib import admin
from .models import *


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'translation']
    list_display_links = ['id', 'text', 'translation']
    search_fields = ['text', 'translation']
    save_on_top = True


@admin.register(DateHistory)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'date']
    list_display_links = ['user', 'date']
    list_filter = ['user', 'date']
    save_on_top = True


@admin.register(TaskHistory)
class TaskHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'task', 'date_start', 'date_last', 'right_answers', 'wrong_answers']
    list_display_links = ['user']
    list_filter = ['user', 'date_start', 'date_last', 'right_answers', 'wrong_answers']
    save_on_top = True


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'next_task']


admin.site.register(Category)

