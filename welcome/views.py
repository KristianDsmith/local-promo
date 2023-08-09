from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def news(request):
    return render(request, 'news.html')


def promo(request):
    return render(request, 'promo.html')


def contact(request):
    return render(request, 'contact.html')


def login(request): 
    return render(request, 'login.html')
