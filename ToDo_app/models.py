from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_user = models.CharField(max_length=20)
    task_status = models.CharField(max_length=15)
