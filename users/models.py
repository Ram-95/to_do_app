from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # Says that a User is associated with one Profile and Vice-versa
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 'profile_pics' here refers to the directory where the profile images are uploaded to
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Method to scale the Uploaded images to our defined resolution - 300 x 300
    # Commenting this code for now because it causes issues when resizing on AWS S3.
    '''
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    '''