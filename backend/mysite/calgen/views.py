import datetime

from django_ical.views import ICalFeed
from rest_framework import generics, status, mixins, viewsets
from rest_framework.response import Response

from .models import Event, CalendarWeek
from .serializers import EventSerializer, CalendarWeekSerializer


# Create your views here.


class CalenderWeekViewsSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CalendarWeek.objects.all()
    serializer_class = CalendarWeekSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request, *args, **kwargs):
        week_id = request.GET.get("weekId")
        if week_id:
            week = CalendarWeek.objects.filter(pk=week_id)
            if not week:
                return Response(
                    data={"message": f"Week with id: {week_id} not found"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            items = Event.objects.filter(week__id=week_id)
            serializer = EventSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class EventViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventViewBulk(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        try:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventFeed(ICalFeed):
    """
    A simple event calendar
    """

    product_id = "-//example.com//Example//EN"
    timezone = "UTC"
    file_name = "event.ics"

    def items(self):
        return Event.objects.all().order_by("-date")

    def item_guid(self, item):
        return "{}{}".format(item.id, "global_name")

    def item_title(self, item):
        return "{}".format(item.name)

    def item_description(self, item):
        return item.description

    def item_start_datetime(self, item):
        return datetime.datetime.combine(item.date, item.start)

    def item_end_datetime(self, item):
        return datetime.datetime.combine(item.date, item.end)

    def item_link(self, item):
        return "http://www.google.de"
