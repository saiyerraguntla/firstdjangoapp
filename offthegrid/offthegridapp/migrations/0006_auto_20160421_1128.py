# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offthegridapp', '0005_auto_20160421_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_id',
            field=models.CharField(max_length=20),
        ),
    ]
