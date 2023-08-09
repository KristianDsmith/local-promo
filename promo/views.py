from django.shortcuts import render


def promo_view(request):
    return render(request, 'promo.html')
