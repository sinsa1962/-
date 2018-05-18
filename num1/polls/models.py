from django.db import models

# Create your models here.

class Intro(models.Model):
    num = models.IntegerField(default =1)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
