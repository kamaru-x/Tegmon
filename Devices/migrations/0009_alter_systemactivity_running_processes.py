# Generated by Django 5.1.3 on 2024-11-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Devices', '0008_alter_device_system_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemactivity',
            name='running_processes',
            field=models.TextField(blank=True, null=True),
        ),
    ]