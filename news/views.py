from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import NewsArticle


def news(request):
    news_articles = NewsArticle.objects.all()
    return render(request, 'news.html', {'news_articles': news_articles})


def like_article(request):
    article_id = request.POST.get('article_id')
    article = NewsArticle.objects.get(pk=article_id)
    article.save()
    return JsonResponse({'like_count': article.likes})

