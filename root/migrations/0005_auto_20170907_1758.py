# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-07 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0004_auto_20170907_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
