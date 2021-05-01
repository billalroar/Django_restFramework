from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import WeatherViewset


router = DefaultRouter()
router.register('data', WeatherViewset, basename='weather-data')
# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]