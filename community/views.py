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
        return redirect('sercices')

    else:
        form = ProfileForm()
    return render(request, 'profile/update_profile.html', {"form": form})
