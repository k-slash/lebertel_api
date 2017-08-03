# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django_countries.fields import CountryField
from easy_thumbnails.fields import ThumbnailerImageField



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
    image = ThumbnailerImageField(upload_to=settings.LEBERTEL_IMAGE_FOLDER, blank=True)
    caption = models.CharField(max_length=200, blank=True)

    #: Use display_order to determine which is the "primary" image
    display_order = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

class UserLocation(models.Model):
    """
    A model which holds information about a particular location
    """
    user = models.OneToOneField(
        'auth.User',
        null=False,
        related_name='location',
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=255)
    postcode = models.CharField(max_length=64)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    country = CountryField()
    location = models.PointField(blank=True)

class UserProfile(models.Model):
    """
    A model which holds information about a particular profile
    """
    user = models.OneToOneField(
        'auth.User',
        null=False,
        related_name='profile',
        on_delete=models.CASCADE
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+262692121212'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    avatar = ThumbnailerImageField(upload_to=settings.LEBERTEL_IMAGE_FOLDER, blank=True)

class UserShowcase(models.Model):
    """
    A model which holds information about a particular showcase
    """
    user = models.OneToOneField(
        'auth.User',
        null=False,
        related_name='showcase',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, blank=True)
    presentation = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = CountryField()
    display_location = models.BooleanField(default=1)
    location = models.PointField(blank=True, null=True)
    display_email = models.BooleanField(default=1)
    email = models.EmailField(max_length=70,blank=True)
    display_phone_number = models.BooleanField(default=1)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+262692121212'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    logo = ThumbnailerImageField(upload_to=settings.LEBERTEL_IMAGE_FOLDER, blank=True)
