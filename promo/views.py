import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from promo.models import UserProfile, Track
from promo.forms import FeedbackForm, SignupForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.conf import settings
from django.http import FileResponse
from promo.models import DownloadableTrack
from django.http import HttpResponseRedirect
from django.db.models import Avg, Count
from django.db.models.functions import TruncDay
from promo.models import Feedback
from django.http import JsonResponse
from django.db.models import F, Count


def promo_view(request):
    signup_form = UserCreationForm()
    login_form = AuthenticationForm()
    return render(request, 'promo.html', {'signup_form': signup_form, 'login_form': login_form})


def profile_view(request, username=None):
    logger.info(f"Entered profile_view with username {username}")
    print(f"Is user authenticated: {request.user.is_authenticated}")
    print(f"username parameter: {username}")

    if request.user.is_authenticated:
        user = request.user
        
        profile = UserProfile.objects.get(user=user)
        track = Track.objects.first()  # or however you want to retrieve the track

        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feedback = form.save(commit=False)
                feedback.user = request.user
                feedback.track = track
                feedback.save()
                return redirect('thank_you', track_id=track.id)
                # Redirect or add a success message
        else:
            form = FeedbackForm()

        return render(request, 'profile.html', {'profile': profile, 'user': user, 'track': track, 'form': form})
    else:
        return redirect('login')


def promo_music_view(request):
    tracks = Track.objects.all()
    feedbacks = Feedback.objects.filter(
        user=request.user).values_list('track_id', flat=True) if request.user.is_authenticated else []

    return render(request, 'promo_music.html', {'tracks': tracks, 'feedbacks': feedbacks})


def feedback_view(request, track_id):
    track = Track.objects.get(pk=track_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.track = track
            feedback.save()
            return redirect('thank_you', track_id=track.id)

    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form, 'track': track})


class MusicTrackListView(ListView):
    model = Track
    template_name = 'music_tracks_list.html'
    context_object_name = 'tracks'


class MusicTrackDetailView(DetailView):
    model = Track
    template_name = 'music_track_detail.html'
    context_object_name = 'track'


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Saving the user
            genre = form.cleaned_data.get('genre')
            country = form.cleaned_data.get('country')
            user_profile, created = UserProfile.objects.get_or_create(
                user=user)
            user_profile.genre = genre
            user_profile.country = country
            user_profile.save()

            # Logging in the user
            login(request, user)

            # Redirect to the user's profile
            return redirect('profile_with_username', username=user.username)

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


logger = logging.getLogger(__name__)


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)

        return redirect(reverse('profile_with_username', kwargs={'username': self.user.username}))


def track_profile(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    return render(request, 'track_profile.html', {'track': track})


def thank_you_view(request, track_id):
    # Using Track instead of DownloadableTrack
    track = get_object_or_404(Track, pk=track_id)
    print(f"Thank you view with track ID: {track_id}")
    return render(request, 'thank_you.html', {'track': track})


def download_music(request, track_id):
    track = get_object_or_404(DownloadableTrack, pk=track_id)
    download_url = track.download_url
    print(f"Track ID: {track_id}, Download URL: {download_url}")
    return HttpResponseRedirect(download_url)


def feedback_dashboard(request):
    # Feedback by user
    feedback_by_user = Feedback.objects.values(
        'user').annotate(count=Count('id'))

    # Average rating
    average_rating = Feedback.objects.aggregate(Avg('rating'))['rating__avg']

    # Feedback count
    feedback_count = Feedback.objects.count()

    # Will play track count
    will_play_count = Feedback.objects.filter(will_play_track=True).count()

    # Country distribution
    country_distribution = Feedback.objects.annotate(
        country=F('user__userprofile__country')
    ).values(
        'country'
    ).annotate(
        count=Count('country')
    )

    # Active users
    active_users = Feedback.objects.values('user').distinct().count()

    # Listened to audio count
    listened_count = Feedback.objects.filter(listened_to_audio=True).count()

    # Downloaded count
    downloaded_count = Feedback.objects.filter(downloaded=True).count()

    context = {
        'feedback_by_user': feedback_by_user,
        'average_rating': average_rating,
        'feedback_count': feedback_count,
        'will_play_count': will_play_count,
        'country_distribution': country_distribution,
        'active_users': active_users,
        'listened_count': listened_count,
        'downloaded_count': downloaded_count,
    }

    return render(request, 'feedback_dashboard.html', context)


def chart_data(request):
    data = {
        'labels': ['January', 'February', 'March'],
        'datasets': [{
            'label': 'Feedback',
            'data': [10, 20, 15],
            # Additional chart settings
        }]
    }
    return JsonResponse(data)
