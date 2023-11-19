from django.db import models
from django import forms


# Create your models here.
class MyModel(models.Model):
    fullname = models.CharField(max_length=200)
    birthday = models.CharField(max_length=10)

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)