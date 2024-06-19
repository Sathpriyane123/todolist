from django.db import models

# Create your models here.

class Task(models.Model):
    Name = models.CharField(max_length=100)
    Task = models.CharField(max_length=100)
