from rest_framework import serializers
from django.contrib.auth.models import User
from to_do.models import Task
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Serializes the User Data and Shows the User Information in JSON format."""
    class Meta:
        model = User
        fields = ('username', 'email')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes the tasks of User and Shows the Tasks of a User in JSON format."""

    class Meta:
        model = Task
        fields = ('task_title', 'is_checked', 'date_posted')
