from django.shortcuts import render
from .serializers import PostSerializer,PostModel,FeedBackSerializer,FeedBackModel
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class PostViews(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

class FeedBackViews(viewsets.ModelViewSet):
    queryset = FeedBackModel.objects.all()
    serializer_class = FeedBackSerializer