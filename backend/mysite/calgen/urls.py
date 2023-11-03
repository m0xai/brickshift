from django.urls import path, re_path

from . import views
from .views import EventFeed

urlpatterns = [
    path("", views.index, name="index"),
    path("event-feed/", views.EventView.as_view(), name="bulk-event-create"),
    re_path(r'^latest/feed.ics$', EventFeed()),
]
