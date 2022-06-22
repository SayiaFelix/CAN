from django.shortcuts import redirect, render


def Home_view(request):
    return render(request,"landing/home.html")