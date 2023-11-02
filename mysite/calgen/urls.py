from django.urls import path, re_path

from . import views
from .views import EventFeed

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^latest/feed.ics$', EventFeed()),
]
