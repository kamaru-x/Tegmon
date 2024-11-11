from django.urls import path
from Devices import views

urlpatterns = [
    path('login/',views.signin,name='login'),
    path('',views.devices,name='devices'),
    path('details/<int:id>/',views.details,name='details'),
]