"""localpromo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from welcome.views import index as welcome_index
from welcome.views import news as your_news_view
from welcome.views import promo as your_promo_view
from welcome.views import contact as your_contact_view
from welcome.views import login as your_login_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_index, name='home'),  # Use welcome_index here
    path('news/', your_news_view, name='news'),
    path('promo/', your_promo_view, name='promo'),
    path('contact/', your_contact_view, name='contact'),
    path('login/', your_login_view, name='login'),
]




    

