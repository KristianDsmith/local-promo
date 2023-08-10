from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile  # Import UserProfile instead of Profile


def save_user_profile(sender, instance, **kwargs):
    if instance.is_superuser:
        return
    instance.profile.save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # Use UserProfile instead of Profile
    UserProfile.objects.get_or_create(user=instance)
