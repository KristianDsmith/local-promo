from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Track(models.Model):
    title = models.CharField(max_length=225)
    artist_name = models.CharField(max_length=225)
    genre = models.CharField(max_length=100, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)  # In seconds
    description = models.TextField(blank=True, null=True)
    cover_image = CloudinaryField(
        'image', blank=True, null=True)  # Image field for cover
    audio_file_url = models.URLField(
        default='https://example.com/default/path/to/file'
    )   # Audio file field

    def __str__(self):
        return self.title


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    rating = models.IntegerField()
    will_play_track = models.BooleanField(default=False)
    listened_to_audio = models.BooleanField(default=False)
    downloaded = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Feedback by {self.user.username} on {self.track.title}"


class DownloadableTrack(models.Model):
    name = models.CharField(max_length=255)
    download_url = models.URLField(
        max_length=500, default="http://example.com/default-url")

    # ... any other fields ...

    def __str__(self):
        return self.name


class ListenedTrack(models.Model):  # New model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    listened_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} listened to {self.track.title}"
