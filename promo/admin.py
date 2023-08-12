from django.contrib import admin
from promo.models import Track
from promo.models import DownloadableTrack
from promo.models import Feedback


class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist_name', 'genre',
                    'release_date', 'duration')


class DownloadableTrackAdmin(admin.ModelAdmin):
    list_display = ['name', 'download_url']


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'track', 'feedback_text', 'rating')


admin.site.register(Track, TrackAdmin)
admin.site.register(DownloadableTrack, DownloadableTrackAdmin)
admin.site.register(Feedback, FeedbackAdmin)
