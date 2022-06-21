from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        exclude = ['type']

class MedicalForm(forms.ModelForm):
    class Meta:
        model = Medical
        exclude = ['address']

class FundForm(forms.ModelForm):
    class Meta:
        model = Fund
        exclude = ['address']

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

