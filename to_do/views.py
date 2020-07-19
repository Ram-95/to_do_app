from django.shortcuts import render
# Imports our Task Model - i.e, Our DB Table
from .models import Task
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

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


def add_new_task(request):
    '''Adds a New Task to the Task Table in Database.'''
    if request.method == 'GET':
        # Getting the task Name from Ajax
        task_name = request.GET['task_title']
        # Dummy User - for the purpose of testing
        creator = User.objects.last()
        # Adding the task to the Database Table - Task
        temp_task = Task(task_title=task_name, author=creator)
        # Saving the changes to the Database
        temp_task.save()
        # Converting the newly added task that is saved to Dictionary format and returning as JSON format
        task_json_string = model_to_dict(temp_task, fields=['id', 'task_title', 'author'])

        # Returning the Saved Tasks details in JSON Format to the AJAX Code.
        # The AJAX Code will then add this task to the Active Tasks Table.
        return JsonResponse(task_json_string)

    else:
        return HttpResponse("Request method is not GET.")


def delete_task(request):
    '''Deletes a task from the Task Table.'''
    if request.method == 'GET':
        # Getting the task_id from AJAX
        task_id = request.GET['task_id']
        # Selecting the task with the given task_id
        del_task = Task.objects.get(id=task_id)
        # Deleting the task from the Table
        del_task.delete()

        return HttpResponse("Deleted the Task")
    else:
        return HttpResponse("Request method is not GET.")