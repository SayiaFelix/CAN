from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    # path('', include('community.urls')),
    path('tinymce/', include('tinymce.urls')),
]

admin.site.site_header= "CAN Administration"
admin.site.site_title="CAN"
