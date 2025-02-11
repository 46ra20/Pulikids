from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import SearchTeacherAndStudent,CourseMaterialView,CourseView

router = DefaultRouter()
router.register(r'add_course',CourseView,basename='course')
router.register(r'material',CourseMaterialView,basename='course_material')
urlpatterns = [
    path('search/<name>/',SearchTeacherAndStudent.as_view({'get':'list'}),name="search"),
    path('course/',include(router.urls),name="add_course")
]
