# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0020_auto_20170828_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='temperature',
            field=models.DecimalField(blank=True, decimal_places=1, default=None, max_digits=3, null=True, verbose_name='Temperature'),
        ),
    ]
