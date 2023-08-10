from django.contrib import admin
from .models import MusicTrack 
from promo.models import Track


class MusicTrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'album', 'genre', 'release_date']
    search_fields = ['title', 'artist']
    list_filter = ['genre']


admin.site.register(MusicTrack, MusicTrackAdmin)
admin.site.register(Track)
