from django.contrib import admin
from .models import PostModel,FeedBackModel,CourseEnrollModel
# Register your models here.

admin.site.register(PostModel)
admin.site.register(FeedBackModel)
admin.site.register(CourseEnrollModel)