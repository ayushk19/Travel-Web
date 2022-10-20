from msilib.schema import Class
from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=30)
    m_num=models.IntegerField()
    messg=models.CharField(max_length=150)

class Signup_login(models.Model):
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    email=models.CharField(max_length=30)
    psswd=models.CharField(max_length=20)