# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from sorl.thumbnail import ImageField

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
    original = models.ImageField(upload_to=settings.LEBERTEL_IMAGE_FOLDER,
        max_length=255)
    caption = models.CharField(max_length=200, blank=True)

    #: Use display_order to determine which is the "primary" image
    display_order = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
