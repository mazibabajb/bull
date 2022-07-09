from email.mime import message
from signal import signal
from unicodedata import name
from unittest import mock
from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sig_cat(models.Model):
    name  = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Analyse(models.Model):
    name  = models.CharField(max_length=100) 
    signal_thumbnail = models.FileField()
    signal_description = models.TextField(max_length=100)
    posted_on = models.DateTimeField(auto_created=True)
    signal_category = models.ForeignKey(Sig_cat,on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class blog_post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    post_description = models.CharField(max_length=300,default="good post") 
    content = models.TextField(max_length=1000)
    category_id =  models.ForeignKey(category,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True)
    is_trending  =  models.BooleanField(default=False)
    thumbnail = models.FileField()


    def __str__(self):
        return self.title


class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email       


class Contact_us(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=400,default="sub")
    message = models.TextField(max_length=500,default="message")

    def __str__(self):
        return self.name         
