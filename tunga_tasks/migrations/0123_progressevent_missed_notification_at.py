# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-03 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_tasks', '0122_summaryreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='progressevent',
            name='missed_notification_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
