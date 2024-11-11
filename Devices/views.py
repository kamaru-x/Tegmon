from django.shortcuts import render,redirect
from Devices.models import Device, SystemActivity
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('devices')
        else:
            return redirect('signin')

    return render(request, 'login.html')

@login_required
def devices(request):
    devices = Device.objects.all()

    context = {
        'devices' : devices
    }
    return render(request,'devices.html',context)

@login_required
def details(request,id):
    device = Device.objects.get(id=id)
    activities = SystemActivity.objects.filter(device=device).order_by('-timestamp')

    context = {
        'device' : device,
        'activities' : activities
    }
    return render(request,'details.html',context)