from django.db import models

# Create your models here.

class Device(models.Model):
    username = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='Active')
    last_check_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username