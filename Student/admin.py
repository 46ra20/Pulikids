from django.contrib import admin
from .models import PostModel,FeedBackModel
# Register your models here.

admin.site.register(PostModel)
admin.site.register(FeedBackModel)