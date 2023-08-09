from django.db import models


class NewsArticle(models.Model):
    headline = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    link = models.URLField()
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.headline
