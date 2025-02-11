from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PostViews,FeedBackViews,CourseEnrollView

router = DefaultRouter()
router.register(r'post',PostViews,basename='post')
router.register(r'feedback',FeedBackViews,basename='feedback')
router.register(r'enroll',CourseEnrollView,basename='enroll')

urlpatterns = [
    path('',include(router.urls),name="public_post")
]
