from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Album,Track
from .serializer import AlbumSerializer,TrackSerializer

# Create your views here.
class AlbumViewset(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        albums = Album.objects.all()
        return albums

class TrackViewset(viewsets.ModelViewSet):
    serializer_class = TrackSerializer

    def get_queryset(self):
        albums = Track.objects.all()
        return albums

