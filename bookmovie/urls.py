"""bookmovie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name='bookmovie'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cam, name='cam'),
    path('bookmovies/',views.movielist ,name='home' ),
    path('bookmovies/movies', views.userlist, name='users'),

    path('occupied/',views.OccupiedSeat, name='seats'),
    path('bookmovies/signup/', views.insertrecord, name='insert'),
    path('bookmovies/login',views.login,name='login'),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
