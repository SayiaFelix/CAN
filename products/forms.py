from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from .models import *


class ProductForm(ModelForm):

    class Meta:
        model = Product
        exclude = ('owner',)  

class BusinessForm(forms.ModelForm):
  class Meta:
      model = Business
      fields = ('business_name','description','business_pic', 'contacts')        





   
