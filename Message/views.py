from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MessageSerializer
from .models import MessageModel
# Create your views here.


class MessageView(viewsets.ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer