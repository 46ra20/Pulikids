from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MessageModel(models.Model):
    text = models.CharField(max_length=300,default="")
    message_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    message_for = models.ForeignKey(User,on_delete=models.CASCADE,related_name="receiver")

    def __str__(self):
        return f'Message by {self.message_by.first_name} {self.message_by.last_name} for {self.message_for.first_name} {self.message_for.last_name}'
    