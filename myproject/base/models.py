from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskModel(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    host=models.ForeignKey(User,on_delete=models.CASCADE)

class HistoryModel(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
