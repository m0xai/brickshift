from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import EventFeed

router = DefaultRouter()
router.register(r"weeks", views.CalenderWeekViewsSet, basename="CalenderWeek")
urlpatterns = [
    path("", include(router.urls)),
    path("events/", views.EventList.as_view(), name="events"),
    path("events/<int:pk>/", views.EventViewDetail.as_view(), name="single-event"),
    path("event-feed/", views.EventViewBulk.as_view(), name="bulk-event-create"),
    # path("weeks/", views.CalenderWeekViewsSet.as_view(), name="weeks"),
    re_path(r"^latest/feed.ics$", EventFeed()),
]
