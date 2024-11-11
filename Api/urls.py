from django.urls import path
from Api import views

urlpatterns = [
    path('devices/', views.DeviceListView.as_view(), name='api-devices'),
    path('device/register/', views.DeviceRegisterView.as_view(), name='device_register'),
    path('activity/', views.SystemActivityView.as_view(), name='system_activity'),
]