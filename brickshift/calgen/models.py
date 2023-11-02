from django.db import models
from django_ical.utils import build_rrule_from_recurrences_rrule
from django_ical.views import ICalFeed
from recurrence.fields import RecurrenceField

from brickshift.base.models import BaseModel

class EventFeed(ICalFeed, BaseModel):
    # Ein Kalender Objekt
    product_id = '-//example.com//Example//EN'
    timezone = 'UTC'

    def file_name(self, obj):
        return "feed_%s.ics" % obj.id

    def items(self):
        return Event.objects.all().order_by('-start_datetime')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_start_datetime(self, item):
        return item.start_datetime

    def item_rrule(self, item):
        """Adapt Event recurrence to Feed Entry rrule."""
        if item.recurrences:
            rules = []
            for rule in item.recurrences.rrules:
                rules.append(build_rrule_from_recurrences_rrule(rule))
            return rules

    def item_exrule(self, item):
        """Adapt Event recurrence to Feed Entry exrule."""
        if item.recurrences:
            rules = []
            for rule in item.recurrences.exrules:
                rules.append(build_rrule_from_recurrences_rrule(rule))
            return rules

    def item_rdate(self, item):
        """Adapt Event recurrence to Feed Entry rdate."""
        if item.recurrences:
            return item.recurrences.rdates

    def item_exdate(self, item):
        """Adapt Event recurrence to Feed Entry exdate."""
        if item.recurrences:
            return item.recurrences.exdates

class Event(BaseModel):
    # Title can be employee's name
    title = models.CharField(max_length=200)
    start = models.TimeField()
    end = models.TimeField()
    recurrences = RecurrenceField()