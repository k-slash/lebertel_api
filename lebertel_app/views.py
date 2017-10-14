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
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, mixins
from lebertel_app.serializers import *
from lebertel_app.models import *
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

class UserConnectedViewSet(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users location to be viewed or edited.
    """
    serializer_class = UserSerializer
    lookup_field = 'id'

    def get_object(self):
        user = self.request.user
        return get_object_or_404(User, id=user.id)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class UserLocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users location to be viewed or edited.
    """
    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSerializer

class UserConnectedLocationView(generics.RetrieveUpdateAPIView):
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

class UserShowcaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users showcase to be viewed or edited.
    """
    queryset = UserShowcase.objects.all()
    serializer_class = UserShowcaseSerializer

class ShowcaseImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products images to be viewed or edited.
    """
    queryset = ShowcaseImage.objects.all()
    serializer_class = ShowcaseImageSerializer

class ShowcaseImageGetView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users location to be viewed or edited.
    """
    serializer_class = ShowcaseImageSerializer

    def get_object(self, pk=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(ShowcaseImage, id=pk)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, pk):
        object.delete()
        return Response(data={'result': "OK"}, status=200)

class ShowcaseImageListView(generics.ListAPIView):
    """
    API endpoint that show image list of one showcase.
    """
    serializer_class = ShowcaseImageSerializer

    def get_queryset(self):
        showcase = self.kwargs.get('showcase_pk')
        return ShowcaseImage.objects.filter(showcase=showcase)


class UserConnectedShowcaseView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users location to be viewed or edited.
    """
    serializer_class = UserShowcaseSerializer
    lookup_field = 'user'

    def get_object(self):
        user = self.request.user
        return get_object_or_404(UserShowcase, user=user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class UserConnectedProfileView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users location to be viewed or edited.
    """
    serializer_class = UserProfileSerializer
    lookup_field = 'user'

    def get_object(self):
        user = self.request.user
        return get_object_or_404(UserProfile, user=user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class UserConnectedProductsListView(generics.ListAPIView):
    """
    API endpoint that show image list of one showcase.
    """
    serializer_class = ProductSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        owner = self.request.user
        return Product.objects.filter(owner=owner)

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users profile to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

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
