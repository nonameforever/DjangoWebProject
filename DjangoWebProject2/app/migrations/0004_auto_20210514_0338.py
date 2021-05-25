# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-14 00:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210514_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 5, 14, 3, 38, 11, 793788), verbose_name='Опубликованно'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 5, 14, 3, 38, 11, 793788), verbose_name='Дата'),
        ),
    ]