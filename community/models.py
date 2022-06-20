from django.db import models
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt



# Create your models here.
class Motivation(models.Model):
    name = models.CharField(max_length=100)
    motiv_photo = models.ImageField(upload_to='motive/')
    motivation = HTMLField()
    target = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Business(models.Model):
    b_photo = models.ImageField(upload_to='bussiness/')
    description = HTMLField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name

class healthservices(models.Model):
    healthservices = models.CharField(max_length=100)

    def __str__(self):
        return self.healthservices

    def save_healthservices(self):
        self.save()

    @classmethod
    def delete_healthservices(cls, healthservices):
        cls.objects.filter(healthservices=healthservices).delete()


class Health(models.Model):
    photo = models.ImageField(upload_to='health/')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    healthservices = models.ManyToManyField(healthservices)

    def __str__(self):
        return self.name


class Security(models.Model):
   
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='post/')
    post = HTMLField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
  
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @classmethod
    def search_post(cls, search_term):
        blogs = cls.objects.filter(title__icontains=search_term)
        return blogs


class Comment(models.Model):
    comment = models.CharField(max_length=300)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

