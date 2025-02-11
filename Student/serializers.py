from rest_framework import serializers
from .models import PostModel,FeedBackModel,CourseEnrollModel

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostModel
        fields = '__all__'

class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackModel
        fields = '__all__'

class CourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollModel
        fields = '__all__'