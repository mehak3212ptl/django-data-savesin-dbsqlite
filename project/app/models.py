from django.db import models

# Create your models here.
class Studentmodel(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Lastname=models.CharField(max_length=50)
    Password=models.IntegerField()
