from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PostViews,FeedBackViews

router = DefaultRouter()
router.register(r'post',PostViews,basename='post')
router.register(r'feedback',FeedBackViews,basename='feedback')

urlpatterns = [
    path('public/',include(router.urls),name="public_post")
]
