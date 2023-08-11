from django.contrib import admin
from .models import Track


class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist_name', 'genre',
                    'release_date', 'duration')


admin.site.register(Track, TrackAdmin)
