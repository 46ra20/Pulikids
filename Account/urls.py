from django.urls import path,include
from .views import StudentRegistrationView,TeacherRegistrationView,LogoutView,LoginView
urlpatterns = [
    path('student/registration/',StudentRegistrationView.as_view(),name='student_registration'),
    path('teacher/registration/',TeacherRegistrationView.as_view(),name='student_registration'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]