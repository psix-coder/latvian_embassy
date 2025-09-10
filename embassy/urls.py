from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ServiceViewSet, MeetingViewSet

router = DefaultRouter()
router.register('services', ServiceViewSet, basename='services')
router.register('meetings', MeetingViewSet, basename='meetings')

urlpatterns = [
    path('', include(router.urls))
]

