from django.contrib import admin
from .models import StudentRegistrationModel,TeacherRegistrationModel
# Register your models here.

admin.site.register(StudentRegistrationModel)
admin.site.register(TeacherRegistrationModel)
