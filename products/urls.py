from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('product/', views.product, name='product'),

    url('search/', views.search, name='search'),
    url('newproduct', views.NewProduct, name='newproduct'),

    url('clothes/', views.clothes, name='clo'),
    url('groceries/', views.groceries, name='groceries'),
    url('shopping/', views.shopping, name='shopping'),
    url('construction/', views.construction, name='construction'),
    

]    