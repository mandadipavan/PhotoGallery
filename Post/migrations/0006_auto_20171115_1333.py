# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 13:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0005_auto_20171111_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 15, 13, 33, 54, 927323, tzinfo=utc)),
        ),
    ]
