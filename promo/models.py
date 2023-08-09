from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class MusicTrack(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='tracks/')
    artwork_image = models.ImageField(upload_to='artwork/')


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
