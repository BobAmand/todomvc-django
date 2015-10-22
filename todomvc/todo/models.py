from django.db import models

# Create your models here.


class Todo(models.Model):
    # id is automatically included.
    task = models.CharField(max_length=100)
    done = models.BooleanField()
    order = models.IntegerField()
