'''This file consists of fields that we want to show in Registration form. We can configure the way we need
But our class should inherit the already existing class - 'UserCreationForm' See 'UserRegisterForm' class
The 'Meta' class is used to tell - "To which model should our form submit data to." Here it is - 'User' Model
'''

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from . models import Profile


class UserRegisterForm(UserCreationForm):
    # Adding a email field in the User Register Form
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    email = forms.EmailField()
    

    class Meta:
        '''This class tells to which model our form data should be submitted. In this case - User Model'''
        model = User
        # The data from these fields is stored in the User Model.
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


# Notify the User when he tries to Reset Password with Incorrect Email
class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = 'There is no user registered with this email address.'
            self.add_error('email', msg)
        return email
