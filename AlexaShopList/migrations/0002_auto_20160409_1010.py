# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AlexaShopList', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('shop_name', models.TextField()),
                ('shop_url', models.TextField()),
                ('shop_product_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchPhrase', models.TextField()),
                ('number', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Offers',
        ),
        migrations.AddField(
            model_name='offer',
            name='search',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlexaShopList.Search'),
        ),
    ]
