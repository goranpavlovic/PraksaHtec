"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from usermanagement.views import MyFirstView, AnotherView, SetMusicianName, SetMusicianCountry, \
                                 MusicianInfo, SongInfo, MusicianViewSet, SongViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'view_music_info', MusicianViewSet, base_name="music")
router.register(r'view_song_info', SongViewSet, base_name="song")

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^another', AnotherView.as_view()),
    url(r'^update-musician', SetMusicianName.as_view()),
    url(r'^country', SetMusicianCountry.as_view()),
    url(r'^music_info', MusicianInfo.as_view()),
    url(r'^song_info', SongInfo.as_view()),
    #url(r'music_info_view', MusicianViewSet),
    #url(r'^song_info_view', SongViewSet),
    url(r'', include(router.urls)),
    #url(r'', MyFirstView.as_view())
]

#urlpatterns += router.urls

#urlpatterns.append()


