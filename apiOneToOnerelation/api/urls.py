from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from apiOneToOnerelation.views import PostsViewSet,PostRatesViewSet

router = DefaultRouter()
router.register('posts', PostsViewSet, basename='posts')
router.register('posts-rates', PostRatesViewSet, basename='posts-rates')
# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]