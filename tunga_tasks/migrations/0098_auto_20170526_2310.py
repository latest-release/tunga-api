# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-26 23:10
from __future__ import unicode_literals

from django.db import migrations, models
import tunga_utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_tasks', '0097_auto_20170523_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskpayment',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='taskpayment',
            name='captured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='taskpayment',
            name='charge_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taskpayment',
            name='currency',
            field=models.CharField(blank=True, choices=[(b'EUR', 'EUR'), (b'USD', 'USD')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='taskpayment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='taskpayment',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='taskpayment',
            name='payment_type',
            field=models.CharField(choices=[(b'stripe', 'Stripe'), (b'bitcoin', 'BitCoin')], default='bitcoin', help_text='stripe - Stripe,bitcoin - BitCoin', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskpayment',
            name='token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='payment_method',
            field=models.CharField(blank=True, choices=[(b'stripe', 'Pay with Stripe'), (b'bitonic', 'Pay with iDeal / mister cash'), (b'bitcoin', 'Pay with BitCoin'), (b'bank', 'Pay by bank transfer')], help_text='stripe - Pay with Stripe,bitonic - Pay with iDeal / mister cash,bitcoin - Pay with BitCoin,bank - Pay by bank transfer', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='taskinvoice',
            name='payment_method',
            field=models.CharField(choices=[(b'stripe', 'Pay with Stripe'), (b'bitonic', 'Pay with iDeal / mister cash'), (b'bitcoin', 'Pay with BitCoin'), (b'bank', 'Pay by bank transfer')], help_text='stripe - Pay with Stripe,bitonic - Pay with iDeal / mister cash,bitcoin - Pay with BitCoin,bank - Pay by bank transfer', max_length=30),
        ),
        migrations.AlterField(
            model_name='taskpayment',
            name='btc_address',
            field=models.CharField(blank=True, max_length=40, null=True, validators=[tunga_utils.validators.validate_btc_address]),
        ),
        migrations.AlterField(
            model_name='taskpayment',
            name='btc_price',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=18, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='taskpayment',
            unique_together=set([('task', 'ref')]),
        ),
    ]
