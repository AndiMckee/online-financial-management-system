# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_company'),
        ('accounts', '0018_auto_20171110_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='workplaces',
        ),
        migrations.AddField(
            model_name='staff',
            name='workplaces',
            field=models.ManyToManyField(null=True, to='companies.Company'),
        ),
    ]