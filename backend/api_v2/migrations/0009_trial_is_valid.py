# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0008_auto_20170101_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='trial',
            name='is_valid',
            field=models.NullBooleanField(db_index=True, default=None, verbose_name='Is Valid?'),
        ),
    ]