from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Devices.urls')),
    path('api/',include('Api.urls')),
]