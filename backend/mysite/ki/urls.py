from rest_framework.routers import DefaultRouter

from .views import WeekPlanViewSet

router = DefaultRouter()
router.register(r'upload', WeekPlanViewSet, basename='weekplan')
urlpatterns = router.urls
