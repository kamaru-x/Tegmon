from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Devices.models import Device, SystemActivity
from Api.serializers import DeviceSerializer, SystemActivitySerializer
from datetime import datetime
from django.utils import timezone

class DeviceListView(APIView):
    def get(self, request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)


class DeviceRegisterView(APIView):
    def post(self, request):
        data = request.data
        system_name = data.get('system_name')
        username = data.get('username')
        ip_address = data.get('ip_address')
        os_version = data.get('os_version')

        if not system_name:
            return Response({"message": "System name is required!"}, status=status.HTTP_400_BAD_REQUEST)

        device, created = Device.objects.get_or_create(system_name=system_name, defaults={
            "username": username,
            "status": "Active",
            "last_login": timezone.now(),
            "ip_address": ip_address,
            "os_version": os_version
        })

        if not created:
            device.last_login = timezone.now()
            device.username = username
            device.ip_address = ip_address
            device.os_version = os_version
            device.save()
            return Response({"message": "Device already registered. Last login updated.", "device": DeviceSerializer(device).data}, status=status.HTTP_200_OK)

        return Response({"message": "Device registered successfully!", "device": DeviceSerializer(device).data}, status=status.HTTP_201_CREATED)

class SystemActivityView(APIView):
    def post(self, request):
        data = request.data
        device_data = data.get('device')
        activity_log = data.get('activity_log')
        running_processes = data.get('running_processes')
        color = data.get('color')

        try:
            device = Device.objects.get(system_name=device_data['system_name'])
        except Device.DoesNotExist:
            return Response({"message": "Device not found!"}, status=status.HTTP_404_NOT_FOUND)

        activity = SystemActivity(
            device=device,
            activity_log=activity_log,
            running_processes=running_processes,
            timestamp=timezone.now(),
            color=color
        )
        activity.save()

        return Response({"message": "Activity logged successfully!"}, status=status.HTTP_201_CREATED)
