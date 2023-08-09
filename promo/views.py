from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MusicTrack, Feedback
from .forms import FeedbackForm


def promo_view(request):
    return render(request, 'promo.html')


def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})


def promo_music_view(request):
    tracks = MusicTrack.objects.all()
    feedbacks = Feedback.objects.filter(
        user=request.user) if request.user.is_authenticated else []

    return render(request, 'promo_music.html', {'tracks': tracks, 'feedbacks': feedbacks})


def feedback_view(request, track_id):
    track = MusicTrack.objects.get(pk=track_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.track = track
            feedback.save()
            # Redirect to music promotion page or a success page
            return redirect('promo_music')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form, 'track': track})


def download_track(request, track_id):
    # Your code to handle downloading the track goes here
    return HttpResponse("Downloading track with ID: " + str(track_id))
