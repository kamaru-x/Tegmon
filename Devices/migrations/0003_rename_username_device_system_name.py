# Generated by Django 5.1.3 on 2024-11-11 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Devices', '0002_device_ip_address_device_os_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='username',
            new_name='system_name',
        ),
    ]
