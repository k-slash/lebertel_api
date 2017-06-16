from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from lebertel_app import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'password')
        write_only_fields = ('password')
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'password')
'''

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserLocation
        country = CountryField()
        geo_field = "point"
        fields = '__all__'

class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Product
        fields = ('owner', 'name', 'price', 'description')
