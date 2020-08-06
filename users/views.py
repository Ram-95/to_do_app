from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import RequestContext
from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# To use login_required decorator
from django.contrib.auth.decorators import login_required
from django.http import Http404


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
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


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
        'p_form': p_form
    }

    return render(request, 'users/edit_profile.html', context)
