from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from ManyToManyR.views import StudentViewSet,ModulesViewSet


router = DefaultRouter()
router.register('student', StudentViewSet, basename='student')
router.register('module', ModulesViewSet, basename='module')
# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]