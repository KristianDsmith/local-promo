from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Track(models.Model):
    profile = models.ForeignKey(
        UserProfile, related_name='tracks', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=225)
    artist_name = models.CharField(max_length=225)
    album = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    cover_image = CloudinaryField('image', blank=True, null=True)
    music_file = CloudinaryField('audio', null=True, blank=True)
    audio_file_url = models.FileField(
        upload_to='tracks/', default='default/path/to/file')
    image = models.ImageField(upload_to='track_images/')

    def __str__(self):
        return self.title


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Feedback by {self.user.username} on {self.track.title}"
