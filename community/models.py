from pydoc import describe
from unicodedata import category
from zoneinfo import available_timezones
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver

Service=(
    ('Driver', 'Driver'),
    ('Doctor', 'Doctor'),
    ('Cleaner', 'Cleaner'),
    ('Teacher', 'Teacher'),
    ('Sponsor', 'Sponsor'),
    ('Motivator', 'Motivator'),
)
Category=(
    ('Sale', 'Sale'),
    ('Donate', 'Donate'),
  
)
Available=(
    ('6:00AM-9:00AM', '6:00AM-9:00AM'),
    ('9:01AM-12:00AM', '9:01AM-12:00AM'),
    ('12:01PM-3:00PM', '12:01PM-3:00PM'),
    ('3:01PM-6:00PM', '3:01PM-6:00PM'),
    ('6:01PM-9:00PM', '6:01PM-9:00PM'),
    ('Emmergencies', 'Emmergencies'),
  
)
Size=(  
    ('XSmall', 'XSmall'),
    ('Small', 'Small'),  
    ('Medium', 'Medium'),
    ('Large','Large'),
    ('XLarge', 'XLarge'), 
)


# Create your models here.
class Services(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='service/')
    description = HTMLField()
    available = models.CharField(max_length=15, choices=Available, default="6:00AM")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cloth(models.Model):
    c_photo = models.ImageField(upload_to='cloth/')
    description = HTMLField()
    size = models.CharField(max_length=15, choices=Size, default="kids")
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=15, choices=Category, default="sell")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name

class medicalservices(models.Model):
    medicalservices = models.CharField(max_length=100)

    def __str__(self):
        return self.medicalservices

    def save_medicalservices(self):
        self.save()

    @classmethod
    def delete_medicalservices(cls, medicalservices):
        cls.objects.filter(medicalservices=medicalservices).delete()


class Medical(models.Model):
    m_photo = models.ImageField(upload_to='medical/')
    daktari = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    medicalservices = models.ManyToManyField(medicalservices)

    def __str__(self):
        return self.name


class Fund(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_photo = models.ImageField(upload_to='profiles/',null=True)
    contact = models.CharField(max_length=12)
    service = models.CharField(max_length=15, choices=Service, default="Driver")
    email = models.EmailField(null=True)
    bio = HTMLField(null=True)
  
    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

        post_save.connect(create_user_profile, sender=User)


    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()

        return profile

    @classmethod
    def find_profile(cls,search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile
        
    def delete_profile(self):
         self.delete()

    def save_profile(self):
        self.save()

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.username
    

   

class Comment(models.Model):
    comment = models.CharField(max_length=300)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    motive = models.ForeignKey(Services, on_delete=models.CASCADE)


