from django.contrib.auth.models import User, Group
from rest_framework import serializers
from lebertel_app import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Product
        fields = ('owner', 'name', 'price', 'description')
