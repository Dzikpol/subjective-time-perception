# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0003_auto_20161006_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='device',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='polarization',
            field=models.CharField(choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical'), ('cross', 'Cross'), ('mixed', 'Mixed')], max_length=15),
        ),
    ]