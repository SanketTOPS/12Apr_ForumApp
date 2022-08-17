from distutils.command.upload import upload
from django.db import models

# Create your models here.

class user_signup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()


class mynotes(models.Model):
    uploaded=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    cate=models.CharField(max_length=100)
    myfile=models.FileField(upload_to="MyFiles")
    comments=models.TextField()

class feedback(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    msg=models.TextField()
