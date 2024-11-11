from rest_framework import serializers
from Devices.models import Device, SystemActivity

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'system_name', 'username', 'last_login', 'ip_address', 'os_version', 'status']

class SystemActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemActivity
        fields = ['id', 'device', 'activity_log', 'running_processes', 'timestamp', 'color']