from django.db import models
from django.contrib.auth.models import User
# Create your models here.
ACCOUNT_TYPE = [
    ('STUDENT','Student'),
    ('TEACHER','Teacher'),
]

class StudentRegistrationModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True,upload_to="Media/Account")
    account_type = models.CharField(choices=ACCOUNT_TYPE,max_length=10)
    department = models.CharField(max_length=30)
    student_id = models.CharField(max_length=12)
    section = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.user.first_name+' '+self.user.last_name
    
class TeacherRegistrationModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True,upload_to="Media/Account")
    account_type = models.CharField(choices=ACCOUNT_TYPE,max_length=10)
    educational_qualification = models.CharField(max_length=20)
    department = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.user.first_name+' '+self.user.last_name

