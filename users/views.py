from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegisterForm
# To use login_required decorator
from django.contrib.auth.decorators import login_required


def register(request):
    '''Registration Form'''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # If the Form is a Valid One
        if form.is_valid():
            # Saves the Data to the Database. I.e creates the User
            form.save()
            username = form.cleaned_data.get('username')
            # Acknowledges the User that the Account is created Successfully
            messages.success(request, f"Your account has been created successfully. You can login now.")
            # Upon Successfully registering the User, redirect to the same 'register.html' page
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
