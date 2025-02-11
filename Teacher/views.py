from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializer import SearchTeacherAndStudentSerializer
from rest_framework.response import Response
from django.db.models import Q
from .serializer import CourseSerializer,CourseMaterialsSerializer,CourseMaterialsModel,CourseModel
# Create your views here.




class SearchTeacherAndStudent(viewsets.ViewSet):
    def list(self,request,name):
        query = User.objects.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        serializer = SearchTeacherAndStudentSerializer(query,many=True)
        return Response(serializer.data)

class CourseMaterialView(viewsets.ModelViewSet):
    queryset = CourseMaterialsModel.objects.all()
    serializer_class = CourseMaterialsSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer


