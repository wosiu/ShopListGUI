# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlexaShopList', '0004_auto_20160409_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='price',
            field=models.FloatField(),
        ),
    ]
