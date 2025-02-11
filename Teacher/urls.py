from django.urls import path
from .views import SearchTeacherAndStudent
urlpatterns = [
    path('search/<name>/',SearchTeacherAndStudent.as_view({'get':'list'}),name="search")
]
