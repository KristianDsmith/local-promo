from django.contrib import admin
from promo.models import Track
from promo.models import DownloadableTrack


class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist_name', 'genre',
                    'release_date', 'duration')


class DownloadableTrackAdmin(admin.ModelAdmin):
    list_display = ['name', 'download_url']


admin.site.register(Track, TrackAdmin)
admin.site.register(DownloadableTrack, DownloadableTrackAdmin)
