# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 20:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 24, 20, 34, 7, 126078, tzinfo=utc)),
        ),
    ]
