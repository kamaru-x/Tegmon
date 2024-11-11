from django.urls import path
from Api import views

urlpatterns = [
    path('devices/', views.DeviceListView.as_view(), name='api-devices'),
    path('register/', views.DeviceRegisterView.as_view(), name='api-register'),
]