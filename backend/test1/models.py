from django.db import models

# Create your models here.

class Tasks (models.Model):
    task = models.CharField(max_length=250)
    key = models.IntegerField()

    def __str__(self):
        return self.task
    