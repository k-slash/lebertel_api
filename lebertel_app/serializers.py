from django.contrib.auth.models import User, Group
from django.conf import settings
from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from easy_thumbnails.templatetags.thumbnail import thumbnail_url
from django.utils.timezone import now
from lebertel_app import models

class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email', 'groups', 'password', 'days_since_joined')
        write_only_fields = ('password')
    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UserLocationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = models.UserLocation
        country = CountryField()
        geo_field = "point"
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    thumb_avatar = serializers.SerializerMethodField('get_thumbnail_avatar')
    thumb_small = serializers.SerializerMethodField('get_thumbnail_s')
    thumb_medium = serializers.SerializerMethodField('get_thumbnail_m')
    thumb_big = serializers.SerializerMethodField('get_thumbnail_b')
    class Meta:
        model = models.UserProfile
        fields = '__all__'
    def get_thumbnail_avatar(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.avatar, 'avatar_crop')
    def get_thumbnail_s(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.avatar, 'small_crop')
    def get_thumbnail_m(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.avatar, 'medium_crop')
    def get_thumbnail_b(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.avatar, 'big_crop')

class UserShowcaseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    logo_small = serializers.SerializerMethodField('get_thumbnail_s')
    logo_medium = serializers.SerializerMethodField('get_thumbnail_m')
    logo_big = serializers.SerializerMethodField('get_thumbnail_b')
    class Meta:
        model = models.UserShowcase
        country = CountryField()
        geo_field = "point"
        fields = '__all__'
    def get_thumbnail_s(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.logo, 'small_crop')
    def get_thumbnail_m(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.logo, 'medium_crop')
    def get_thumbnail_b(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.logo, 'big_crop')

class ShowcaseImageSerializer(serializers.ModelSerializer):
    thumb_small = serializers.SerializerMethodField('get_thumbnail_s')
    thumb_medium = serializers.SerializerMethodField('get_thumbnail_m')
    thumb_big = serializers.SerializerMethodField('get_thumbnail_b')
    url = serializers.SerializerMethodField('get_thumbnail_b_crop')
    class Meta:
        model = models.ShowcaseImage
        fields = '__all__'
    def get_thumbnail_s(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.image, 'small')
    def get_thumbnail_m(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.image, 'medium')
    def get_thumbnail_b(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.image, 'big')
    def get_thumbnail_b_crop(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.image, 'big_crop')

class ProductImageSerializer(serializers.ModelSerializer):
    thumb_small = serializers.SerializerMethodField('get_thumbnail_s')
    thumb_medium = serializers.SerializerMethodField('get_thumbnail_m')
    thumb_big = serializers.SerializerMethodField('get_thumbnail_b')
    url = serializers.SerializerMethodField('get_thumbnail_b_crop')
    class Meta:
        model = models.ProductImage
        fields = '__all__'
    def get_thumbnail_s(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.image, 'small')
    def get_thumbnail_m(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.image, 'medium')
    def get_thumbnail_b(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.image, 'big')
    def get_thumbnail_b_crop(self, obj):
        return settings.SITE_URL + thumbnail_url(obj.image, 'big_crop')

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = models.Product
        fields = '__all__'
