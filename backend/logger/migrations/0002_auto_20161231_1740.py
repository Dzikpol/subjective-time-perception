# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 17:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requestlogger',
            options={'verbose_name': 'Request', 'verbose_name_plural': 'Requests'},
        ),
    ]
