from rest_framework import serializers
from Devices.models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'username', 'status', 'last_check_in']