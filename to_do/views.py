from django.shortcuts import render
# Imports our Task Model - i.e, Our DB Table
from .models import Task
from django.http import HttpResponse
from django.contrib.auth.models import User

user = User.objects.first()

def home(request):
    context = {
        # Shows the tasks of a particular User
        # 'tasks': user.task_set.all()
        # Shows all the tasks from the DB
        'tasks': Task.objects.all()
    }
    return render(request, 'to_do_app/home.html', context)

def test(request):
    return render(request, 'to_do_app/test.html')

def mark_as_done(request):
    ''' Function that Marks a task as Completed. Updates the 'is_checked' attribute to 'True'.'''
    if request.method == 'GET':
        # Get the task_id from the checked Checkbox
        task_id = request.GET['task_id']
        # Select the Task whose id matches with task_id
        done_task = Task.objects.get(pk=task_id)
        # Update the 'is_checked' attribute to True. i.e, Mark as Done
        done_task.is_checked = True
        # Save the update to the Database
        done_task.save()

        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not GET.")

