from django.shortcuts import render
from django.http import HttpResponse
from django_ical.views import ICalFeed

from .models import Event


# Create your views here.

def index(request):
    return HttpResponse("Hello World")

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
        return item.date

    def item_link(self, item):
        return "http://www.google.de"