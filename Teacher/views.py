from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializer import SearchTeacherAndStudentSerializer
from rest_framework.response import Response
from django.db.models import Q
# Create your views here.


# def SearchTeacherAndStudent(request,name):
#         print(name)
#         query = User.objects.filter(first_name = name)
#         return HttpResponse("query")


class SearchTeacherAndStudent(viewsets.ViewSet):
    def list(self,request,name):
        query = User.objects.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        serializer = SearchTeacherAndStudentSerializer(query,many=True)
        return Response(serializer.data)


