from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import AlbumViewset,TrackViewset

router = DefaultRouter()
router.register('album', AlbumViewset, basename='album')
router.register('track', TrackViewset, basename='track')
# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]