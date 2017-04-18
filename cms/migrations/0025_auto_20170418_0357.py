# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 03:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0024_auto_20170418_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageshome',
            name='page_link',
        ),
        migrations.AddField(
            model_name='messageshome',
            name='link',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]