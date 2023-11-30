from django.db import models

# Create your models here.
class WeekPlan(models.Model):
    calendar_week = models.IntegerField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='images')