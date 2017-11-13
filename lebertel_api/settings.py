"""
Django settings for lebertel_api project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_93n@ds$7sm5d-vr7y#)$e7=c3%@dh4r$$ejf_=$ss_9(^74$)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_COOKIE_NAME = "csrftoken"


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django_extensions',
    'django_filters',
    'compressor',
    'widget_tweaks',
    'oauth2_provider',
    'rest_framework',
    'rest_framework_gis',
    'corsheaders',
    'sorl.thumbnail',
    'easy_thumbnails',
    'django_countries',
    'lebertel_api',
    'lebertel_app'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lebertel_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lebertel_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
#'ENGINE': 'django.db.backends.postgresql_psycopg2',

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'lebertel_db',
        'USER': 'postgres',
        'PASSWORD': 'Stjo97480',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)

STATICFILES_DIR = {
    os.path.join(BASE_DIR, 'static')
}

SITE_URL = 'http://localhost:8000'
STATIC_URL = '/static/'
STATIC_ROOT = location('static')
MEDIA_URL = '/media/'
MEDIA_ROOT = location('media')
THUMBNAIL_DEBUG = True
THUMBNAIL_KEY_PREFIX = 'oscar-sandbox'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

LEBERTEL_IMAGE_FOLDER = 'images/%Y/%m/'

AUTH_USER_MODEL = 'auth.User'

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

THUMBNAIL_ALIASES = {
    '': {
        'avatar_crop': {'size': (120, 120), 'crop': True},
        'small_crop': {'size': (250, 250), 'crop': True},
        'medium_crop': {'size': (500, 500), 'crop': True},
        'big_crop': {'size': (1000, 1000), 'crop': True},
        'avatar': {
            'size': (120, 0),
            'autocrop': True,
            'crop': 'smart',
            'upscale': True,
        },
        'small': {
            'size': (250, 0),
            'autocrop': True,
            'crop': 'smart',
            'upscale': True,
        },
        'medium': {
            'size': (500, 0),
            'autocrop': True,
            'crop': 'smart',
            'upscale': True,
        },
        'big': {
            'size': (1000, 0),
            'autocrop': True,
            'crop': 'smart',
            'upscale': True,
        }
    },
}
