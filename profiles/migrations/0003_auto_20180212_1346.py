# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-12 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170907_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='activated',
            field=models.BooleanField(default=True),
        ),
    ]
