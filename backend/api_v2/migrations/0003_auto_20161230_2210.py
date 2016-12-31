# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0002_auto_20161230_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='device',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experiment',
            name='location',
            field=models.CharField(db_index=True, default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experiment',
            name='start',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
