from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Devices.models import Device
from Api.serializers import DeviceSerializer
from datetime import datetime

class DeviceListView(APIView):
    def get(self, request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

class DeviceRegisterView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')

        if not username:
            return Response({"message": "Username is required!"}, status=status.HTTP_400_BAD_REQUEST)

        existing_device = Device.objects.filter(username=username).first()

        if existing_device:
            return Response({"message": "Device already registered!"}, status=status.HTTP_400_BAD_REQUEST)

        device = Device(username=username, status="Active", last_check_in=datetime.now())
        device.save()

        return Response({"message": "Device registered successfully!"}, status=status.HTTP_201_CREATED)
