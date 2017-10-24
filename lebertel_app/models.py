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
    short_description = models.CharField(max_length=200, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    size = models.CharField(max_length=200, blank=True, null=True, default=None)
    colors = models.CharField(max_length=200, blank=True, null=True, default=None)
    materials = models.CharField(max_length=200, blank=True, null=True, default=None)

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
        primary_key=True,
        related_name='location',
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=255, blank=True, null=True, default=None)
    postcode = models.CharField(max_length=64, blank=True, null=True, default=None)
    city = models.CharField(max_length=100, blank=True, null=True, default=None)
    state = models.CharField(max_length=100, blank=True, null=True, default=None)
    country = CountryField(default='RE')
    location = models.PointField(blank=True, null=True, default=None)

class UserProfile(models.Model):
    """
    A model which holds information about a particular profile
    """
    user = models.OneToOneField(
        'auth.User',
        primary_key=True,
        related_name='profile',
        on_delete=models.CASCADE
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+262692121212'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True, default=None)
    avatar = ThumbnailerImageField(upload_to=settings.LEBERTEL_IMAGE_FOLDER, blank=True, null=True, default=None)

class UserShowcase(models.Model):
    """
    A model which holds information about a particular showcase
    """
    user = models.OneToOneField(
        'auth.User',
        primary_key=True,
        related_name='showcase',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, blank=True, null=True, default=None)
    presentation = models.TextField(blank=True, null=True, default=None)
    address = models.CharField(max_length=255, blank=True, null=True, default=None)
    postcode = models.CharField(max_length=64, blank=True, null=True, default=None)
    city = models.CharField(max_length=100, blank=True, null=True, default=None)
    state = models.CharField(max_length=100, blank=True, null=True, default=None)
    country = CountryField(default='RE')
    display_location = models.BooleanField(default=1)
    location = models.PointField(blank=True, null=True, default=None)
    display_email = models.BooleanField(default=1)
    email = models.EmailField(max_length=70, blank=True, null=True, default=None)
    display_phone_number = models.BooleanField(default=1)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+262692121212'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True, default=None)
    facebook = models.CharField(max_length=255, blank=True, null=True, default=None)
    linkedin = models.CharField(max_length=255, blank=True, null=True, default=None)
    twitter = models.CharField(max_length=255, blank=True, null=True, default=None)
    pinterest = models.CharField(max_length=255, blank=True, null=True, default=None)
    timetable = models.TextField(blank=True, null=True, default=None)
    informations = models.TextField(blank=True, null=True, default=None)
    logo = ThumbnailerImageField(upload_to=settings.LEBERTEL_IMAGE_FOLDER, blank=True, null=True, default=None)

class ShowcaseImage(models.Model):
    """
    An image of a showcase
    """
    showcase = models.ForeignKey(
        'UserShowcase',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='showcases')
    image = ThumbnailerImageField(upload_to=settings.LEBERTEL_IMAGE_FOLDER, blank=True)
    caption = models.CharField(max_length=200, blank=True)

    #: Use display_order to determine which is the "primary" image
    display_order = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
