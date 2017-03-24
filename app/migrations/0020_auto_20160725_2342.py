# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 22:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20160725_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='')),
                ('education', models.TextField()),
                ('work', models.TextField()),
                ('social_facebook', models.CharField(max_length=256)),
                ('social_twitter', models.CharField(max_length=256)),
                ('social_instagram', models.CharField(max_length=256)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='follow',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='time'),
        ),
        migrations.AlterField(
            model_name='vehiclesharing',
            name='arrival_time',
            field=models.TimeField(max_length=256, verbose_name='estimated arrivak'),
        ),
        migrations.AlterField(
            model_name='vehiclesharing',
            name='details',
            field=models.TextField(verbose_name='ride details'),
        ),
    ]
