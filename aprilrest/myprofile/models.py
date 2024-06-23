from django.db import models

# Create your models here.
class userprofile(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    adres=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=20)