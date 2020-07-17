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


def move_tasks(request):
    ''' Function to move the tasks from Active Table to Complete Table and vice-versa. '''
    if request.method == 'GET':
        # Gets the Task's ID from the checkbox that is clicked
        task_id = request.GET['task_id']
        # Gets the Task's Class name from the checkbox that is clicked
        task_class = request.GET['task_class']
        # If the Clicked Task is an Active Task - Move it from Active Table to Complete Table
        if 'mark_as_done' in task_class:
            # Select the Task whose id matches with task_id
            done_task = Task.objects.get(pk=task_id)
            # Update the 'is_checked' attribute to True. i.e, Mark as Done
            done_task.is_checked = True
            # Save the changes to the Database
            done_task.save()

        # If the Clicked Task is a Complete Task - Move it from Complete Table to Active Table
        elif 'mark_as_undone' in task_class:
            # Select the task matching with the task_id
            undone_task = Task.objects.get(pk=task_id)
            # Update the 'is_checked' attribute to 'False' i.e, Mark as Undone
            undone_task.is_checked = False
            # Save the changes to the Database
            undone_task.save()

        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not GET.")
