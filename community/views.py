from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from .models import *
# from .forms import *
import datetime as datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse

def services(request):
    return render(request,"Hood/services.html")
