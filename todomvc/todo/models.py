from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField()
    order = models.IntegerField()
