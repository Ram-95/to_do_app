from django.shortcuts import render
# Imports our 'Task' Model(Table) - i.e, Our Table in the Database
from .models import Task
from django.db.models import Max
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):
    '''The first page of Application.'''
    return render(request, 'to_do_app/index.html')


# Using function based views
@csrf_exempt
def tasks(request):
    # Gets the Currently Logged In user
    current_user = request.user
    # Getting the Latest date - The date when the user made a modification
    max_date = current_user.task_set.all().aggregate(
        max_date=Max('date_posted'))['max_date']
    # print(f'Current User: {current_user.username}')
    context = {
        # Shows the tasks of a particular User
        # 'tasks': user.task_set.all()
        # Shows all the tasks from the DB
        'tasks': current_user.task_set.all(),
        'max_date': max_date
    }
    return render(request, 'to_do_app/tasks.html', context)


'''
This is the way to add decorators to Class Based Views
More Info - https://docs.djangoproject.com/en/3.1/topics/class-based-views/intro/#decorating-the-class
'''
decorators = [csrf_exempt, login_required]


@method_decorator(decorators, name='dispatch')
class TaskListView(ListView):
    ''' Using Class based view - ListView '''
    model = Task
    template_name = 'to_do_app/tasks.html'  # <app_name>/<model>_<viewtype>.html
    context_object_name = 'tasks'

    def get_queryset(self):
        '''Returns the tasks of the currently logged in User'''
        current_user = self.request.user
        return current_user.task_set.all()


def test(request):
    return render(request, 'to_do_app/test.html')


'''
# API view - Shows all the Tasks in JSON Format
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
'''


@csrf_exempt
@login_required
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
@login_required
def add_new_task(request):
    '''Adds a New Task to the Task Table in Database.'''
    if request.method == 'POST':
        # Getting the task Name from Ajax
        task_name = request.POST['task_title'].strip()
        # Dummy User - for the purpose of testing
        creator = request.user
        # Adding the task to the Database Table - Task
        temp_task = Task(task_title=task_name, author=creator)
        # Saving the changes to the Database
        temp_task.save()
        # Converting the newly added task that is saved to Dictionary format and returning as JSON format
        task_json_string = model_to_dict(
            temp_task, fields=['id', 'task_title', 'author'])

        # Returning the Saved Tasks details in JSON Format to the AJAX Code.
        # The AJAX Code will then add this task to the Active Tasks Table.
        return JsonResponse(task_json_string)

    else:
        return HttpResponse("Request method is not GET.")

# Using csrf_exempt decorator - To tell the view not to check the csrf_token.


@csrf_exempt
@login_required
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
@login_required
def delete_all_completed_tasks(request):
    '''Deletes all the Completed tasks from the Completed Table'''
    if request.method == 'POST':
        # Getting the Tasks that are Marked as Completed - i.e, Tasks that have is_checked == 1
        del_tasks = Task.objects.filter(is_checked=1)
        # Deleting the Completed Tasks
        del_tasks.delete()
        # print('Deleted all Completed Tasks')
        return HttpResponse("Successfully Deleted all Completed Tasks")
    else:
        return HttpResponse("Request is not POST.")


@csrf_exempt
@login_required
def update_task(request):
    '''Updates the task'''
    if request.method == 'POST':
        # Getting the Task ID of the task to be updated from AJAX Call
        task_id = request.POST['task_id']
        # Getting the modified Task name from AJAX Call
        new_task = request.POST['task_name']
        # Querying the Task model to get the task based on task_id
        changed_task = Task.objects.get(id=task_id)
        # Updating the Task Name with the NEW Value
        changed_task.task_title = new_task.strip()
        # Saving the changes to the Database
        changed_task.save()
        # For Debugging Purpose
        print(f'Task Updated ID: {task_id}')
        return HttpResponse("Successfully Updated Tasks")
    else:
        return HttpResponse('Request is not POST.')


@csrf_exempt
@login_required
def refresh_data(request):
    '''Returns the updated data after every AJAX Call.'''
    if request.method == 'POST':
        # Getting the username of the User requested
        user = request.user
        # Converting the user's tasks to JSON format
        data = serializers.serialize("json", user.task_set.all())
        # Return the JSON string. Will work only if safe is set to 'False'
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse('Request Method is not POST.')
