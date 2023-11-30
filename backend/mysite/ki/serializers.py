from rest_framework import serializers

from .models import WeekPlan


class WeekPlanSerializer(serializers.ModelSerializer):
    calendar_week = serializers.IntegerField(max_value=52, min_value=1)
    year = serializers.IntegerField(max_value=2050, min_value=2000)

    class Meta:
        model = WeekPlan
        fields = ["calendar_week", "year", "image"]
