from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # Says that a User is associated with one Profile and Vice-versa
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 'profile_pics' here refers to the directory where the profile images are uploaded to
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'







