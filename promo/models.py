from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username
        
class MusicTrack(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255, blank=True, null=True)  # Optional
    genre = models.CharField(max_length=100, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)  # Optional
    cover_image = CloudinaryField('image', blank=True, null=True)  # Optional
    music_file = CloudinaryField('audio', null=True, blank=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(MusicTrack, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Feedback by {self.user.username} on {self.track.title}"


class Track(models.Model):
    image = models.ImageField(upload_to='tracks/images/')
    title = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)
    release_date = models.DateField()
    info = models.TextField()
    audio_file = models.FileField(upload_to='tracks/audio/')

    def __str__(self):
        return self.title
