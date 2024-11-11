from django.shortcuts import render
from Devices.models import Device

# Create your views here.

def devices(request):
    devices = Device.objects.all()

    context = {
        'devices' : devices
    }
    return render(request,'devices.html',context)