from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CourseMaterialsModel,CourseModel,BlockModel

class SearchTeacherAndStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['id','first_name','last_name']


class CourseMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
         model = CourseMaterialsModel
         fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'
    

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockModel
        fields = '__all__'