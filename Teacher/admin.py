from django.contrib import admin
from .models import CourseMaterialsModel,CourseModel
# Register your models here.

admin.site.register(CourseModel)
admin.site.register(CourseMaterialsModel)
