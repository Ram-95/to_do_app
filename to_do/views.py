from django.shortcuts import render
# Imports our 'Task' Model(Table) - i.e, Our Table in the Database
from .models import Task
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.forms.models import model_to_dict


def index(request):
    '''The first page of Application.'''
    return render(request, 'to_do_app/index.html')

@csrf_exempt
def tasks(request):
    # Gets the Currently Logged In user
    current_user = request.user
    # print(f'Current User: {current_user.username}')
    context = {
        # Shows the tasks of a particular User
        # 'tasks': user.task_set.all()
        # Shows all the tasks from the DB
        'tasks': current_user.task_set.all()
    }
    return render(request, 'to_do_app/tasks.html', context)


def test(request):
    return render(request, 'to_do_app/test.html')

@csrf_exempt
def move_tasks(request):
    ''' Function to move the tasks from Active Table to Complete Table and vice-versa. '''
    if request.method == 'POST':
        # Gets the Task's ID from the checkbox that is clicked
        task_id = request.POST['task_id']
        # Gets the Task's Class name from the checkbox that is clicked
        task_class = request.POST['task_class']
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

@csrf_exempt
def add_new_task(request):
    '''Adds a New Task to the Task Table in Database.'''
    if request.method == 'POST':
        # Getting the task Name from Ajax
        task_name = request.POST['task_title']
        # Dummy User - for the purpose of testing
        creator = request.user
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

# Using csrf_exempt decorator - To tell the view not to check the csrf_token.
@csrf_exempt
def delete_task(request):
    '''Deletes a task from the Task Table.'''
    if request.method == 'POST':
        # Getting the task_id from AJAX
        task_id = request.POST['task_id']
        # Selecting the task with the given task_id
        del_task = Task.objects.get(id=task_id)
        # Deleting the task from the Table
        del_task.delete()
        print(f'Deleted the Task with ID: {task_id}')
        return HttpResponse("Deleted the Task")
    else:
        return HttpResponse("Request method is not POST.")

@csrf_exempt
def delete_all_completed_tasks(request):
    '''Deletes all the Completed tasks from the Completed Table'''
    if request.method == 'POST':
        # Getting the Tasks that are Marked as Completed - i.e, Tasks that have is_checked == 1
        del_tasks = Task.objects.filter(is_checked=1)
        # Deleting the Completed Tasks
        del_tasks.delete()
        print('Deleted all Completed Tasks')
        return HttpResponse("Successfully Deleted all Completed Tasks")
    else:
        return HttpResponse("Request is not POST.")


@csrf_exempt
def refresh_data(request):
    '''Returns the Updated Data in JSON format to the AJAX Call as Response.'''
    if request.method == 'POST':
        data = serializers.serialize('json', request.user.task_set.all())
        print('Data Refresh Request Received')
        #return JsonResponse(data, safe=False)
        return HttpResponse('Data Refresh Successful.')
    else:
        return HttpResponse('Request method is not POST')
