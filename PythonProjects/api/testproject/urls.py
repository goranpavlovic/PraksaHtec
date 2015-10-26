"""testproject URL Configuration

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
from mytestapp.views import GetUser, MusicianInfo, PlayersView, PlayersViewTwo,\
                            PlayersRegularSeasonView, PlayersPlayoffView, PlayersAllStarView, PlayersImageView,\
                            PlayersCareerView, TeamSeasonView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get-user/', GetUser.as_view()),
    url(r'^get-musician/', MusicianInfo.as_view()),
    url(r'^get-player/', PlayersView.as_view()),
    url(r'^get-players/', PlayersViewTwo.as_view()),
    url(r'^get-regular/', PlayersRegularSeasonView.as_view()),
    url(r'^get-playoff/', PlayersPlayoffView.as_view()),
    url(r'^get-allstar/', PlayersAllStarView.as_view()),
    url(r'^get-image/', PlayersImageView.as_view()),
    url(r'^get-career/', PlayersCareerView.as_view()),
    url(r'^get-team-season/', TeamSeasonView.as_view())
]
