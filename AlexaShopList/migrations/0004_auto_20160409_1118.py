# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 11:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AlexaShopList', '0003_auto_20160409_1025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='searchPhrase',
            new_name='search_phrase',
        ),
    ]
