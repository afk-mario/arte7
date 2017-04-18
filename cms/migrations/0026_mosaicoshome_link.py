# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 05:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0025_auto_20170418_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='mosaicoshome',
            name='link',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
