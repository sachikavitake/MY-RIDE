# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 00:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160708_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleSharing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=256, verbose_name='starting point')),
                ('dest', models.CharField(max_length=256, verbose_name='destination')),
                ('cost', models.IntegerField(max_length=256, verbose_name='cost')),
                ('start_time', models.TimeField(max_length=256, verbose_name='start time')),
                ('arrival_time', models.TimeField(max_length=256, verbose_name='starting point')),
                ('no_pass', models.CharField(max_length=256, verbose_name='no of passengers')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=30, verbose_name='gender preference')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='category',
            field=models.CharField(choices=[('car', 'car'), ('bus', 'bus'), ('coaster', 'coaster'), ('Truck', 'Truck')], max_length=30, verbose_name='vehicle category'),
        ),
        migrations.AddField(
            model_name='vehiclesharing',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Vehicle'),
        ),
    ]
