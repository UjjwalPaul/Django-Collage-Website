from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

# class Profile(models.Model)
      # table name      inhareite krna pdega models.Model
class registrationData(models.Model):
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    mail = models.CharField(max_length=40)
    mob = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    dob = models.DateField()
    pass1 = models.CharField(max_length=50) 
    gender = models.CharField(max_length=10)

def __str__(self):
    f = self.name
    return f

 