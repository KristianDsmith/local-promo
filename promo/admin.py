from django.contrib import admin
from .models import MusicTrack 



class MusicTrackAdmin(admin.ModelAdmin):  # Define the admin class for MusicTrack
    list_display = ('title', 'artist',)

admin.site.register(MusicTrack, MusicTrackAdmin)
