from datetime import date

from django.db import models
from recurrence.fields import RecurrenceField


# Create your models here.
class BasicModel(models.Model):
    name = models.CharField(max_length=255)

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    date = models.DateField(default=date.today)
    start = models.TimeField()
    end = models.TimeField()
    recurrence = RecurrenceField()

    def __str__(self):
        return self.name