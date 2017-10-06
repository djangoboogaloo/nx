from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    email_confirmed = models.BooleanField(default=False)
    otp=models.CharField(max_length=6,blank=True)
    balance= models.BigIntegerField(default=99)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except AttributeError:
        profile = Profile.objects.create(user=instance)

        profile.save()
