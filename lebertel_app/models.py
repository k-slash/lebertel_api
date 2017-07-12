# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.conf import settings
from sorl.thumbnail import ImageField
from django_countries.fields import CountryField


# Create your models here.
class Product(models.Model):
    owner = models.ForeignKey(
        'auth.User',
        null=False,
        related_name='products',
        on_delete=models.CASCADE)
    name     = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    price    = models.FloatField()
    description = models.TextField(blank=True)

class ProductImage(models.Model):
    """
    An image of a product
    """
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='products')
    image = ImageField(upload_to=settings.LEBERTEL_IMAGE_FOLDER, blank=True)
    caption = models.CharField(max_length=200, blank=True)

    #: Use display_order to determine which is the "primary" image
    display_order = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

class UserLocation(models.Model):
    """
    A model which holds information about a particular location
    """
    user = models.ForeignKey(
        'auth.User',
        null=False,
        related_name='location',
        on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    postcode = models.CharField(max_length=64)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    country = CountryField()
    location = models.PointField(blank=True)
