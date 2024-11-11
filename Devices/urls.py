from django.urls import path
from Devices import views

urlpatterns = [
    path('',views.devices,name='devices')
]