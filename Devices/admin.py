from django.contrib import admin
from Devices.models import Device

# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id','username','last_check_in']

admin.site.register(Device, DeviceAdmin)