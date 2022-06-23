from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def product(request):
    return render(request,"product.html") 

@login_required
def search(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_product = Product.search_by_products(search_term)
        message = search_term

        return render(request,'search.html',{"message":message,
                                             "searched_product":searched_product})
    else:
        message = "You haven't searched for any product"
        return render(request,'search.html',{"message":message})   

@login_required
def NewProduct(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = current_user
            product.save()
        return redirect('product')
        
    else:
        form = ProductForm()
    return render(request, 'newproduct.html', {"form":form, "current_user":current_user})

@login_required
def NewBusiness(request):
    current_user = request.user
    business = Business.objects.filter(business=current_user)
    if request.method == 'POST':
        businessform = BusinessForm(request.POST, request.FILES)
        if businessform.is_valid():
            business = businessform.save(commit=False)
            business.user = request.user
            business.save()
        return redirect('product')
   

    return render(request, 'business.html', {"business":business})

@login_required
def clothes(request):
    return render(request,"clothes.html")  

@login_required
def groceries(request):
    return render(request,"groceries.html")     

@login_required
def shopping(request):
    return render(request,"shopping.html")  

@login_required
def construction(request):
    return render(request,"construction.html") 

                   
