from django.contrib import admin
from django.urls import path
from car.views import CarsAPIView

urlpatterns = [
    path('cars/', CarsAPIView.as_view()),
]