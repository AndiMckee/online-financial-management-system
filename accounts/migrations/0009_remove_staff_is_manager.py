# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20171109_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='is_manager',
        ),
    ]
