# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-12 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_tasks', '0141_auto_20171128_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='distribution_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='progressevent',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Update'), (2, 'Periodic Update'), (3, 'Milestone'), (4, 'Final Draft'), (5, 'Submission'), (6, 'PM Report'), (7, 'Client Survey'), (8, 'Internal Milestone')], default=1, help_text='1 - Update,2 - Periodic Update,3 - Milestone,4 - Final Draft,5 - Submission,6 - PM Report,7 - Client Survey,8 - Internal Milestone'),
        ),
        migrations.AlterField(
            model_name='taskpayment',
            name='payment_type',
            field=models.CharField(choices=[(b'stripe', 'Stripe'), (b'bitcoin', 'BitCoin'), (b'bank', 'Bank Transfer')], help_text='stripe - Stripe,bitcoin - BitCoin,bank - Bank Transfer', max_length=30),
        ),
    ]
