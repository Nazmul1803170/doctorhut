from pyexpat import model
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.contrib.auth.models import User
# Create your models here.

class DoctorList(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=20)




