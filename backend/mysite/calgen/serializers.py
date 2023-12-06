from rest_framework import serializers

from .models import Event, CalenderWeek


class CalenderWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalenderWeek
        fields = ["id", "year", "number", "start", "end"]


class EventSerializer(serializers.ModelSerializer):
    week = CalenderWeekSerializer
    class Meta:
        model = Event
        fields = ["id", "name", "description", "date", "start", "end", "week"]
