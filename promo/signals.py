from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile  # Import UserProfile instead of Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_superuser:
        return
    # Use get_or_create to either get the existing profile or create a new one
    UserProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_superuser:
        return
    if hasattr(instance, 'profile'):
        instance.profile.save()
