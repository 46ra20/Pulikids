from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializer import SearchTeacherAndStudentSerializer
from rest_framework.response import Response
from django.db.models import Q
from .serializer import CourseSerializer,CourseMaterialsSerializer,CourseMaterialsModel,CourseModel,BlockModel,BlockSerializer
from Student.models import CourseEnrollModel
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

class BlockView(viewsets.ModelViewSet):
    queryset = BlockModel.objects.all()
    serializer_class = BlockSerializer


def RemoveStudent(request,student_id,course_id):
    print(course_id,student_id)
    queries = CourseEnrollModel.objects.filter(Q(pk=course_id))
    for query in queries:
        if query.enroll_by.pk==student_id:
            query.delete()
            return HttpResponse({"status":"success","message":"Successfully Removed"})
    
    return HttpResponse({"status":"failed","message":"Didn't find any course with this information"})
