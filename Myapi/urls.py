"""Myapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from firstapp.views import firstFunction
from rest_framework.routers import DefaultRouter
from firstapp.views import CarSpecsViewset
from ManyToManyR.api import urls

router = DefaultRouter()
router.register('car_space', CarSpecsViewset, basename='car-specs')
# urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first-app/first/',firstFunction ),
    path('', include(router.urls)),
    path('car-app/', include('car.api.urls')),
    path('post-app/', include('apiOneToOnerelation.api.urls')),
    path('school/', include('ManyToManyR.api.urls')),
    path('GTArace/', include('GTArace.urls')),
    path('music/', include('Album.urls')),
    path('weather/', include('Weather.urls')),
]
