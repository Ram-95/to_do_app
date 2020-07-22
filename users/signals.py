# This is fired when a object is saved
from django.db.models.signals import post_save
# We want to get a post_save signal when a User is created
from django.contrib.auth.models import User
# To receive the signal by the post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''Creates a Profile.'''
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    '''Saves a Profile'''
    instance.profile.save()

