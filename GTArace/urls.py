from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import DriverViewSet

router = DefaultRouter()
router.register('driver', DriverViewSet, basename='driver')

urlpatterns = [
    path('', include(router.urls)),
]