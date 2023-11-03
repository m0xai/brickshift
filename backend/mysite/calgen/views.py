import datetime
from django.http import HttpResponse
from django_ical.views import ICalFeed
from rest_framework import generics, status, mixins
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer


# Create your views here.

def index(request):
    return HttpResponse("Hello World")

class EventView(generics.ListCreateAPIView, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        #! This overrides create for multiple event objects and we should clear all events before create EventFeed
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        try:
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventFeed(ICalFeed):
    """
    A simple event calender
    """
    product_id = '-//example.com//Example//EN'
    timezone = 'UTC'
    file_name = "event.ics"

    def items(self):
        return Event.objects.all().order_by('-date')

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