# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-01 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_tasks', '0048_task_skype_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]