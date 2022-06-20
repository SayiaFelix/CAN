from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class MotivationForm(forms.ModelForm):
    class Meta:
        model = Motivation
        exclude = ['name']
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ClothForm(forms.ModelForm):
    class Meta:
        model = Cloth
        exclude = ['owner']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['username', 'cloth','motive']

