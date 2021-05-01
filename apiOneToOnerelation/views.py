from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from apiOneToOnerelation.models import PostsRates,Posts
from .serializer import PostsSerializer,PostsRatesSerializer
# Create your views here.


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostsSerializer

    def get_queryset(self):
        post = Posts.objects.all
        return Posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_rate = PostsRates.objects.create(likes=post_data['rates']['like'],dislike=post_data['rates']['dislike'])
        new_rate.save()
        new_post = Posts.objects.create(post_title=post_data['post_title'],
        post_body=post_data['post_body'],rates=new_rate)
        new_post.save()

        serializer = PostsSerializer(new_post)

        return Response(serializer.data)
        
    
class PostRatesViewSet(viewsets.ModelViewSet):
    serializer_class = PostsRatesSerializer

    def get_queryset(self):
        rates = PostsRates.objects.all()
        return rates