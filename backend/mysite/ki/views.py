from django.http import HttpResponse
from rest_framework import viewsets, mixins

from .models import WeekPlan
from .serializers import WeekPlanSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello World")


class WeekPlanViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = WeekPlan.objects.all()
    serializer_class = WeekPlanSerializer
