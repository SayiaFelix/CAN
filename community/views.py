from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
import datetime as datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse

def services(request):
    return render(request,"services.html")


def profile(request,profile_id):
     current_user = request.user
     try:
      profile = Profile.objects.get(user=current_user)

     except Profile.DoesNotExist:
      profile = None
     return render(request,"profile/profile.html",{"profile":profile})


def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('services')

    else:
        form = ProfileForm()
    return render(request, 'profile/update_profile.html', {"form": form})

def clothes(request):
  
    clothes = Cloth.objects.all

    return render(request, 'ser_clothes.html', {"clothes": clothes})

def add_clothes(request):
    current_user = request.user
   
    try:
     profile = Profile.objects.get(user=current_user)

    except Profile.DoesNotExist:
      profile = None

    if request.method == "POST":
        form = ClothForm(request.POST, request.FILES)
        if form.is_valid():
            cloth = form.save(commit=False)
            cloth.owner = current_user
            cloth.save()

        return HttpResponseRedirect('information')

    else:
        form = ClothForm()

    return render(request, 'ser_cloth_add.html', {"form":form})


def motivation(request):
    current_user = request.user
    try:
        
     profile = Profile.objects.get(user=current_user)

    except Profile.DoesNotExist:
      profile = None

    motivation = Motivation.objects.all

    return render(request, 'motivation.html', {"motivation":motivation})

def add_motivation(request):
    current_user = request.user
   
    try:
     profile = Profile.objects.get(user=current_user)

    except Profile.DoesNotExist:
      profile = None

    if request.method == "POST":
        form = MotivationForm(request.POST, request.FILES)
        if form.is_valid():
            motive = form.save(commit=False)
            motive.user = current_user
            motive.save()

        return HttpResponseRedirect('motivation')

    else:
        form = MotivationForm()

    return render(request, 'ser_motive_add.html', {"form":form})


def medical(request):
    current_user = request.user
   
    try:
     profile = Profile.objects.get(user=current_user)

    except Profile.DoesNotExist:
      profile = None

    medicalservices = Medical.objects.all

    return render(request, 'medical.html', {"medicalservices":medicalservices})

def fund(request):
    current_user = request.user
    try:
     profile = Profile.objects.get(user=current_user)

    except Profile.DoesNotExist:
      profile = None

    informations = Motivation.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'Hood/info.html', {"informations":informations})

