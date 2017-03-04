# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-04 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_tasks', '0059_auto_20170304_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.IntegerField(choices=[(1, 'Web'), (2, 'Mobile'), (3, 'Other')], default=3),
        ),
    ]
