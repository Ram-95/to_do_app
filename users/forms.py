'''This file consists of fields that we want to show in Registration form. We can configure the way we need
But our class should inherit the already existing class - 'UserCreationForm' See 'UserRegisterForm' class
The 'Meta' class is used to tell - "To which model should our form submit data to." Here it is - 'User' Model
'''

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile


class UserRegisterForm(UserCreationForm):
    # Adding a email field in the User Register Form
    email = forms.EmailField()

    class Meta:
        '''This class tells to which model our form data should be submitted. In this case - User Model'''
        model = User
        # The data from these fields is stored in the User Model.
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
