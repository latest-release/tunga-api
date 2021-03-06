# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-17 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_pages', '0003_auto_20170714_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillpage',
            old_name='story_body',
            new_name='story_body_one',
        ),
        migrations.RenameField(
            model_name='skillpage',
            old_name='story_image',
            new_name='story_interlude_one_image',
        ),
        migrations.AddField(
            model_name='skillpage',
            name='story_body_three',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skillpage',
            name='story_body_two',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skillpage',
            name='story_interlude_one_cta',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skillpage',
            name='story_interlude_one_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skillpage',
            name='story_interlude_two_image',
            field=models.ImageField(blank=True, null=True, upload_to='pages/uploads/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='skillpage',
            name='story_interlude_two_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
