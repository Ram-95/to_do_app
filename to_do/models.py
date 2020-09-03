from django.db import models
# Utility that stores the date and time in our Timezone
from django.utils import timezone
# Imports the User - This maps the Task to the Users of our App.(Users as in Admin console)
from django.contrib.auth.models import User


# This is similar to Creating a DB Table with attributes and Data Types
class Task(models.Model):
    '''Creates a Table called 'Task' in the Database. Contains the definition of Table and it's attributes.'''
    # Stores the Title of the Task - Restricted to 60 Characters
    task_title = models.CharField(max_length=60)

    # Stores the Checked status i.e, if the check box is checked or not; 0 - Not Checked; 1 -Checked
    is_checked = models.BooleanField(default=False)

    # Denotes when the task is added - Updates the Current Date and Time
    date_posted = models.DateTimeField(auto_now=True)

    # If a author is deleted, then all his tasks will also be deleted since CASCADE option is set
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title

    class Meta:
        ordering = ('-date_posted',)
