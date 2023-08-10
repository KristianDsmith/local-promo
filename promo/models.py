from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


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


def download_track(request, track_id):
    track = MusicTrack.objects.get(pk=track_id)
    if Feedback.objects.filter(user=request.user, track=track).exists():
        # Provide download
        file_path = track.audio_file.path
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(file_path)
            return response
    else:
        # Redirect to feedback page
        return HttpResponseRedirect('/path/to/feedback/page')
