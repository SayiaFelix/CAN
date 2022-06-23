from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
  
    url('services/', views.services, name='services'),
    url('search/', views.search, name='search'),
  
    url('profile/(\d+)', views.profile, name = 'profile'),
    url('update/profile', views.update_profile, name = 'update-profile'),

    url('information', views.clothes, name='clothes'),
    url('new/info', views.add_clothes, name = 'add_info'),

    url('motivation', views.motivation, name='motivation'),
    url('new/motive', views.add_motivation, name = 'add_motive'),

    url('add/funds', views.donate_funds, name='donate_funds'),

    url('medical', views.medical, name='medicalservices'),
    url('add/health', views.add_medical, name='add_medic'),

   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)