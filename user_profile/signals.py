from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from plant.models import MyProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MyProfile.objects.create(user=instance)
