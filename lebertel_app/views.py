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
from rest_framework.parsers import FileUploadParser
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, mixins
from lebertel_app.serializers import *
from lebertel_app.models import *
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class HomeShowcaseSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 1000

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
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
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
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    lookup_field = 'slug_name'
    queryset = UserShowcase.objects.all()
    serializer_class = UserShowcaseSerializer
    pagination_class = HomeShowcaseSetPagination

class UserShowcaseByIdViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users showcase to be viewed or edited.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = UserShowcase.objects.all()
    serializer_class = UserShowcaseSerializer
    pagination_class = HomeShowcaseSetPagination

class AllUserShowcaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users showcase to be viewed or edited.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = UserShowcase.objects.all()
    serializer_class = UserShowcaseSerializer
    pagination_class = None

class ShowcaseImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products images to be viewed or edited.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = ShowcaseImage.objects.all()
    serializer_class = ShowcaseImageSerializer
    pagination_class = None

class ShowcaseImageGetView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows showcase images to be viewed or edited.
    """
    serializer_class = ShowcaseImageSerializer
    pagination_class = None

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
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = ShowcaseImageSerializer
    pagination_class = None

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

class UserAvatarUploadView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users location to be viewed or edited.
    """
    serializer_class = UserProfileSerializer
    lookup_field = 'user'

    def get_object(self):
        user = self.request.user
        return get_object_or_404(UserProfile, user=user)

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class UserShowcaseLogoUploadView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users location to be viewed or edited.
    """
    serializer_class = UserShowcaseSerializer
    lookup_field = 'user'

    def get_object(self):
        user = self.request.user
        return get_object_or_404(UserShowcase, user=user)

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class ShowcaseUpdateNbViews(generics.ListAPIView):
    """
    API endpoint that allows update showcase number views.
    """
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserShowcaseNbViewsSerializer
    pagination_class = None

    def get_queryset(self):
        user = self.kwargs.get('showcase_pk')
        return UserShowcase.objects.filter(user=user)

    def put(self, request, *args, **kwargs):
        user = self.kwargs.get('showcase_pk')
        showcase = UserShowcase.objects.get(user=user)
        showcase.nb_views = request.data['nb_views']
        showcase.save(update_fields=['nb_views'])
        return Response()

class ShowcaseUpdateNbLikes(generics.ListAPIView):
    """
    API endpoint that allows update showcase number views.
    """
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserShowcaseNbViewsSerializer
    pagination_class = None

    def get_queryset(self):
        user = self.kwargs.get('showcase_pk')
        return UserShowcase.objects.filter(user=user)

    def put(self, request, *args, **kwargs):
        user = self.kwargs.get('showcase_pk')
        showcase = UserShowcase.objects.get(user=user)
        showcase.nb_likes = request.data['nb_likes']
        showcase.save(update_fields=['nb_likes'])
        return Response()

class UserConnectedProductsListView(generics.ListAPIView):
    """
    API endpoint that show image list of one showcase.
    """
    serializer_class = ProductSerializer
    lookup_field = 'owner'
    pagination_class = None

    def get_queryset(self):
        owner = self.request.user
        return Product.objects.filter(owner=owner)

class UserProductsListView(generics.ListAPIView):
    """
    API endpoint that show image list of one showcase.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = ProductSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        owner = self.kwargs.get('user_id')
        return Product.objects.filter(owner=owner)

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users profile to be viewed or edited.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
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
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    #lookup_field = 'uuid'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = HomeShowcaseSetPagination

class AllProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    #lookup_field = 'uuid'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = None

class ProductImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products images to be viewed or edited.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    pagination_class = None

class ProductImageListView(generics.ListAPIView):
    """
    API endpoint that show image list of one showcase.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = ProductImageSerializer
    pagination_class = None

    def get_queryset(self):
        product = self.kwargs.get('product_pk')
        return ProductImage.objects.filter(product=product)

class ProductImageGetView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users location to be viewed or edited.
    """
    serializer_class = ProductImageSerializer
    pagination_class = None

    def get_object(self, pk=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(ProductImage, id=pk)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, pk):
        object.delete()
        return Response(data={'result': "OK"}, status=200)

class ProfessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    pagination_class = None
    queryset = Profession.objects.all().order_by('name')
    serializer_class = ProfessionSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category',)
