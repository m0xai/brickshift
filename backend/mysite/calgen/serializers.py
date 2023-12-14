from rest_framework import serializers

from .models import Event, CalendarWeek


class CalendarWeekSerializer(serializers.ModelSerializer):
    start = serializers.DateField()
    end = serializers.DateField()

    class Meta:
        model = CalendarWeek
        fields = ["id", "year", "number", "start", "end"]


class EventSerializer(serializers.ModelSerializer):
    week = CalendarWeekSerializer
    date = serializers.DateField()
    start = serializers.TimeField()
    end = serializers.TimeField()

    class Meta:
        model = Event
        fields = ["id", "name", "description", "date", "start", "end", "week"]
