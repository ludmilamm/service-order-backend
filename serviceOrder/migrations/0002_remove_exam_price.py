# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-18 01:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceOrder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='price',
        ),
    ]
