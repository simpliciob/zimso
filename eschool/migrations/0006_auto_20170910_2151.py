# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 20:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eschool', '0005_auto_20170910_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fee',
            old_name='Student_number',
            new_name='student_number',
        ),
    ]
