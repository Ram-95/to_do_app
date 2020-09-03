from rest_framework import viewsets, generics
# To Show "Not Found" when queryset returns None in API
from rest_framework.exceptions import NotFound
from .serializers import ProfileSerializer, TaskSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import RequestContext
from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# To use login_required decorator
from django.contrib.auth.decorators import login_required
from django.http import Http404
from to_do.models import Task
from django.contrib.auth.models import User


# API End Point - Shows all the Users data
class ProfileViewSet(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        uname = self.kwargs['username']
        user = User.objects.filter(username=uname).first()
        if user is not None:
            return User.objects.filter(username=user)
        else:
            raise NotFound()


# API End Point - Shows the task of a particular User
class TaskViewSet(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        uname = self.kwargs['username']
        user = User.objects.filter(username=uname).first()
        # print(f'{user.id}')
        if user is not None:
            return Task.objects.filter(author=user.id)
        else:
            raise NotFound()


def register(request):
    '''Registration Form'''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # If the Form is a Valid One
        if form.is_valid():
            # Saves the Data to the Database. I.e creates the User
            form.save()
            # username = form.cleaned_data.get('username')
            fname = form.cleaned_data.get('first_name')
            # Acknowledges the User that the Account is created Successfully
            # messages.success(request, f"Hey {username}, Your account has been created successfully. You can login now.")
            messages.add_message(
                request, messages.SUCCESS, f"Hey {fname}, Your account has been created successfully. You can login now.")
            # Upon Successfully registering the User, redirect to login page
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Register'})


@login_required
def profile(request):
    # Gets the Currently Logged In user
    current_user = request.user
    # print(f'Current User: {current_user.username}')
    fname = User.objects.filter(username=current_user).first().first_name
    lname = User.objects.filter(username=current_user).first().last_name
    context = {
        # Shows the tasks of a particular User
        # 'tasks': user.task_set.all()
        # Shows all the tasks from the DB
        'tasks': current_user.task_set.all(),
        'active_count': Task.objects.filter(author=current_user, is_checked=False).count(),
        'completed_count': Task.objects.filter(author=current_user, is_checked=True).count(),
        'title': current_user,
        'name': fname + ' ' + lname

    }

    return render(request, 'users/profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # print(request.user.username)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # Acknowledges the User that the Account is Updated Successfully
            messages.add_message(request, messages.INFO,
                                 f"Your details have been saved succesfully.")
            # Redirect the User to his Profile
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Edit Profile'
    }

    return render(request, 'users/edit_profile.html', context)
