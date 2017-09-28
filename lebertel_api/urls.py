"""lebertel_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from lebertel_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'products/images', views.ProductImageViewSet)
router.register(r'userShowcases', views.UserShowcaseViewSet)
router.register(r'userLocations', views.UserLocationViewSet)
router.register(r'userProfiles', views.UserProfileViewSet)
router.register(r'showcases/images', views.ShowcaseImageViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('^user/$', views.UserConnectedViewSet.as_view()),
    url('^user/profile/', views.UserConnectedProfileView.as_view()),
    url('^user/location/', views.UserConnectedLocationView.as_view()),
    url('^user/showcase/', views.UserConnectedShowcaseView.as_view()),
    url('^showcases/(?P<showcase_pk>[0-9]+)/images/', views.ShowcaseImageListView.as_view()),
    url('^showcases/(?P<showcase_pk>[0-9]+)/images/(?P<pk>[0-9]+)$', views.ShowcaseImageGetView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
