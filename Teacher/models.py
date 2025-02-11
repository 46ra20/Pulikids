from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CourseMaterialsModel(models.Model):
    file = models.FileField(upload_to="Media/Materials")
    upload_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'File upload by {self.upload_by.first_name} {self.upload_by.last_name}'

class CourseModel(models.Model):
    course_title = models.CharField(max_length=200,default="")
    course_thumbnail = models.ImageField(upload_to="Media/Thumbnail",null=True,blank=True)
    materials = models.ManyToManyField(CourseMaterialsModel)
    description = models.TextField()
    course_credit = models.IntegerField(default=0)
    course_created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'Course created by {self.course_created_by.first_name} {self.course_created_by.last_name}'


class BlockModel(models.Model):
    is_blocked = models.BooleanField(default=False)
    block_student = models.ForeignKey(User,on_delete=models.CASCADE,related_name="block_student")
    block_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="block_by")

    def __str__(self):
        return f'{self.block_student.first_name} {self.block_student.last_name} block by {self.block_by.first_name} {self.block_by.last_name}'
