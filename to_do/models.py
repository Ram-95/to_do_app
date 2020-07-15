from django.db import models
# Utility that stores the date and time in our Timezone
from django.utils import timezone
# Imports the User - This maps the Task to the Users of our App.(Users as in Admin console)
from django.contrib.auth.models import User


class Task(models.Model):
    # Stores the Title of the Task
    task_title = models.CharField(max_length=60)

    # Stores the Checked status i.e, if the check box is checked or not; 0 - Not Checked; 1 -Checked
    is_checked = models.IntegerField(default=0)

    # Denotes when the task is added - Updates the Current Date and Time
    date_posted = models.DateTimeField(default=timezone.now)

    # If a author is deleted, then all his posts will also be deleted since CASCADE
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title

