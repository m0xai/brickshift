from datetime import date

from django.db import models


# Create your models here.
class BasicModel(models.Model):
    name = models.CharField(max_length=255)


class CalendarWeek(models.Model):
    year = models.IntegerField()
    number = models.IntegerField()
    start = models.DateField()
    end = models.DateField()


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="", null=True)
    date = models.DateField(default=date.today)
    start = models.TimeField()
    end = models.TimeField()
    week = models.ForeignKey(CalendarWeek, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
