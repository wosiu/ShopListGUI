from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Search(models.Model):
    search_phrase = models.TextField(null = True)
    number = models.IntegerField(null = True)
    date = models.DateField(null=True)
    chosen_offer = models.ForeignKey('Offer', related_name='+', null=True)


class Offer(models.Model):
    price = models.FloatField(null=True)
    shop_name = models.TextField(null=True)
    shop_url = models.TextField(null=True)
    shop_product_name = models.TextField(null=True)
    image_link = models.TextField(null=True)
    search = models.ForeignKey(Search, related_name='+', null=True)

