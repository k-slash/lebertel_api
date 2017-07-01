# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from lebertel_app.serializers import UserSerializer, GroupSerializer, ProductSerializer, ProductImageSerializer, UserLocationSerializer
from lebertel_app.models import Product, ProductImage, UserLocation
from rest_framework import filters



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email',)

class UserLocationViewSet(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users location to be viewed or edited.
    """
    serializer_class = UserLocationSerializer
    lookup_field = 'user'

    def get_object(self):
        user = self.request.user
        return get_object_or_404(UserLocation, user=user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products images to be viewed or edited.
    """
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
