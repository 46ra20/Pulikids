from rest_framework import serializers
from .models import PostModel,FeedBackModel

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostModel
        fields = '__all__'

class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackModel
        fields = '__all__'