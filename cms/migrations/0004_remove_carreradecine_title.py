# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 23:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_carreradecine_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carreradecine',
            name='title',
        ),
    ]