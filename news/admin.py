from django.contrib import admin
from .models import NewsArticle


class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('headline',)


admin.site.register(NewsArticle, NewsArticleAdmin)
