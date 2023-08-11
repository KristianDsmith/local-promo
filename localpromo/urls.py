"""localpromo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from welcome.views import index as welcome_index, news as your_news_view, promo as your_promo_view, contact as your_contact_view, login as your_login_view
from promo.views import profile_view, promo_music_view, feedback_view, download_track, MusicTrackListView, MusicTrackDetailView, signup_view, CustomLoginView, track_profile
from promo.models import Track
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_index, name='home'),
    path('news/', your_news_view, name='news'),
    path('promo/', your_promo_view, name='promo'),
    path('contact/', your_contact_view, name='contact'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', profile_view, name='profile_with_username'),
    path('promo_music/', promo_music_view, name='promo_music'),
    path('feedback/<int:track_id>/', feedback_view, name='feedback_view'),
    path('download/<int:track_id>/', download_track, name='download_track'),
    path('music/', MusicTrackListView.as_view(), name='track_list'),
    path('music/<int:pk>/', MusicTrackDetailView.as_view(), name='track_detail'),
    path('signup/', signup_view, name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('track/<int:track_id>/', track_profile, name='track_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
