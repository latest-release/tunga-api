# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-05 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_tasks', '0132_sprint'),
    ]

    operations = [
        migrations.AddField(
            model_name='workactivity',
            name='completed',
            field=models.NullBooleanField(default=None),
        ),
    ]
