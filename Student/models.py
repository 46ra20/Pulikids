from django.db import models
from django.contrib.auth.models import User
from Teacher.models import CourseModel

# Create your models here.

USER_RATING = [
    ('1','★'),
    ('2','★★'),
    ('3','★★★'),
    ('4','★★★★'),
    ('5','★★★★★')
]

class PostModel(models.Model):
    description = models.TextField(default="",null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to="Media/Post")
    post_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'Post By {self.post_by.first_name} {self.post_by.last_name}'

class FeedBackModel(models.Model):
    feedback = models.TextField(default="")
    ratting = models.CharField(choices=USER_RATING,max_length=5)
    feedback_for = models.ForeignKey(CourseModel,on_delete=models.CASCADE,default=0)
    feedback_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'Feedback By {self.feedback_by.first_name} {self.feedback_by.last_name}'


class CourseEnrollModel(models.Model):
    course = models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    enroll_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course.course_title} enrolled by {self.enroll_by.first_name} {self.enroll_by.last_name}'

