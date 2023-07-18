from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = ['title', 'description']


admin.site.register(Task, TaskAdmin)