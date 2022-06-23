from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Product(models.Model):
    itemname = models.CharField(max_length=50)
    description = models.CharField(max_length = 200,null = True)
    price=models.CharField(max_length = 200, blank=True)
    contacts=models.IntegerField(blank=True)
    product_pic = models.ImageField(upload_to="product_pic", null=True)
    

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)

    
    def __str__(self):
        return self.itemname

class Business(models.Model):
    business_name = models.CharField(max_length=50)
    contacts =models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    business_pic = models.ImageField(upload_to="business_pic", null=True)
    
    def __str__(self):
        return self.business_name

    # create business
    def create_business(self):
        self.save()

    # delete business
    def delete_business(self):
        self.delete()

    # update business
    def update_business(self):
        self.update()        

              