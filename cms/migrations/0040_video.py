# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 22:06
from __future__ import unicode_literals

import cms.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0039_merge_20170517_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=cms.models.upload_to_video)),
                ('thumbnail', models.ImageField(upload_to=cms.models.upload_to_thumbnail)),
            ],
        ),
    ]
