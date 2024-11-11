from django.db import models

# Create your models here.

class Device(models.Model):
    status = models.CharField(max_length=50, default='Active')
    system_name = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=25)
    os_version = models.CharField(max_length=25)

    def __str__(self):
        return self.system_name


class SystemActivity(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    activity_log = models.TextField()  # Stores user actions
    running_processes = models.TextField(null=True, blank=True)  # Stores running processes
    timestamp = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=10,default='gray')

    def __str__(self):
        return f"Activity on {self.device.system_name} at {self.timestamp}"