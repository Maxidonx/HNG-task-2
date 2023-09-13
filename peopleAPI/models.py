from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50, unique=True)
    track = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname
    

