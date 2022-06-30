from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
import datetime as datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse

def services(request):
    return render(request,"service/services.html")

@login_required
def profile(request,profile_id):
     current_user = request.user
     try:
      profile = Profile.objects.get(user=current_user)

     except Profile.DoesNotExist:
      profile = None
     return render(request,"profile/profile.html",{"profile":profile})

@login_required
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

    return render(request, 'service/cloth.html', {"clothes": clothes})

@login_required
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

    return render(request, 'service/add_cloth.html', {"form":form})


def motivation(request):
    motivation = Services.objects.all

    return render(request, 'service/service.html', {"motivation":motivation})

@login_required
def add_motivation(request):
    current_user = request.user
   
    try:
     profile = Profile.objects.get(user=current_user)

    except Profile.DoesNotExist:
      profile = None

    if request.method == "POST":
        form = ServicesForm(request.POST, request.FILES)
        if form.is_valid():
            motive = form.save(commit=False)
            motive.user = current_user
            motive.save()

        return HttpResponseRedirect('motivation')

    else:
        form = ServicesForm()

    return render(request, 'service/add_service.html', {"form":form})


def medical(request):
    medicalservices = Medical.objects.all
    return render(request, 'service/medical.html', {"medicalservices":medicalservices})

@login_required
def add_medical(request):
    current_user = request.user
   
    try:
     profile = Profile.objects.get(user=current_user)

    except Profile.DoesNotExist:
      profile = None

    if request.method == "POST":
        form = MedicalForm(request.POST, request.FILES)
        if form.is_valid():
            medical = form.save(commit=False)
            medical.user = current_user
            medical.save()

        return HttpResponseRedirect('medical')

    else:
        form = MedicalForm()

    return render(request, 'service/add_medical.html', {"form":form})

@login_required
def donate_funds(request):
    current_user = request.user
   
    try:
     profile = Profile.objects.get(user=current_user)

    except Profile.DoesNotExist:
      profile = None

    if request.method == "POST":
        form = FundForm(request.POST, request.FILES)
        if form.is_valid():
            fund = form.save(commit=False)
            fund.name = current_user
            fund.save()

        messages.success(request,f'Thanks for your support.')
        return HttpResponseRedirect('services')

    else:
        form = FundForm()

    return render(request, 'service/donate_fund.html', {"form":form})

@login_required
def search(request):
    current_user = request.user
    profile = Profile.get_profile()
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_name = Profile.find_profile(search_term)
        message = search_term

        return render(request,'service/search.html',{"message":message,"profiles":profile,"user":current_user,"username":searched_name})
    else:
        message = "You haven't searched for any username"
        return render(request,'service/search.html',{"message":message})



