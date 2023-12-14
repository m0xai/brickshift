from rest_framework import serializers

from .models import Event, CalendarWeek


class CalendarWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarWeek
        fields = ["id", "year", "number", "start", "end"]


class EventSerializer(serializers.ModelSerializer):
    week = CalendarWeekSerializer

    class Meta:
        model = Event
        fields = ["id", "name", "description", "date", "start", "end", "week"]
