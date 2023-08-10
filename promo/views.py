from django.shortcuts import render, redirect
from django.http import HttpResponse
from promo.models import MusicTrack, Feedback
from promo.forms import FeedbackForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from promo.forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def promo_view(request):
    signup_form = UserCreationForm()
    login_form = AuthenticationForm()
    return render(request, 'promo.html', {'signup_form': signup_form, 'login_form': login_form})


def profile_view(request):
    user_profile = request.user.profile
    # You can access additional fields on the UserProfile model here
    return render(request, 'profile.html', {'profile': user_profile})


def promo_music_view(request):
    tracks = MusicTrack.objects.all()
    feedbacks = Feedback.objects.filter(
        user=request.user).values_list('track_id', flat=True) if request.user.is_authenticated else []

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


class MusicTrackListView(ListView):
    model = MusicTrack
    template_name = 'music_tracks_list.html'
    context_object_name = 'tracks'


class MusicTrackDetailView(DetailView):
    model = MusicTrack
    template_name = 'music_track_detail.html'
    context_object_name = 'track'


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False          # Ensure the user is not staff
            user.is_superuser = False      # Ensure the user is not a superuser
            user.save()                    # Now save the user
            login(request, user)           # Log the user in
            messages.success(
                request, 'Your account has been created successfully. You are now logged in.')
            # Redirect to the profile page only for regular users
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
