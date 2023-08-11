from django.contrib import admin
from .models import Track


class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist_name', 'album', 'genre', 'release_date']
    search_fields = ['title', 'artist_name']
    list_filter = ['genre']


admin.site.register(Track, TrackAdmin)
