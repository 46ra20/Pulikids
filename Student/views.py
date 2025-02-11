from django.shortcuts import render
from .serializers import PostSerializer,PostModel,FeedBackSerializer,FeedBackModel,CourseEnrollModel,CourseEnrollSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class PostViews(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

class FeedBackViews(viewsets.ModelViewSet):
    queryset = FeedBackModel.objects.all()
    serializer_class = FeedBackSerializer

class CourseEnrollView(viewsets.ModelViewSet):
    queryset = CourseEnrollModel.objects.all()
    serializer_class = CourseEnrollSerializer