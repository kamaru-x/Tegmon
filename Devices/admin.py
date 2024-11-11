from django.contrib import admin
from Devices.models import Device, SystemActivity

# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id','system_name','username','last_login','os_version','ip_address']

admin.site.register(Device, DeviceAdmin)

class SystemActivityAdmin(admin.ModelAdmin):
    list_display = ['id','device','activity_log','running_processes','timestamp']

admin.site.register(SystemActivity, SystemActivityAdmin)