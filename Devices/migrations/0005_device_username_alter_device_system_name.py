# Generated by Django 5.1.3 on 2024-11-11 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Devices', '0004_rename_last_check_in_device_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='username',
            field=models.CharField(default='Kamaru', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='system_name',
            field=models.CharField(max_length=50),
        ),
    ]
