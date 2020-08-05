from django.urls import reverse
from django.contrib import admin
from django.utils.http import urlencode
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    '''Overrides the list show in the Task section of Admin'''
    # Lists the Id, Task name and the Completed status of the Task
    list_display = ("id", "task_title", "is_checked")
    # Shows a filter based on the author
    list_filter = ("author",) 