from django.urls import path, re_path

from . import views
from .views import  EventFeed

urlpatterns = [
    path("", views.index, name="index"),
    path("events/", views.EventList.as_view(), name="events"),
    path('events/<int:pk>/', views.EventViewDetail.as_view(), name="single-event"),
    path("event-feed/", views.EventViewBulk.as_view(), name="bulk-event-create"),
    re_path(r'^latest/feed.ics$', EventFeed()),
]
