# -*- coding: utf-8 -*-
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')fcdl05yy4qn3)+_gb2_p#9n4a!8cnwa+t2^umz2itl491)lv6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
PRODUCTION = False

# Application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webview',
    'webview.templatetags'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware'
)

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_microforum',
        'USER': 'postgres',
        'PASSWORD': '010203',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# E-mail
EMAIL_HOST = "xxx"
EMAIL_HOST_USER = "xxx"
EMAIL_HOST_PASSWORD = "xxx"
EMAIL_USE_TLS = True

# Internationalization
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('en-us', u'English'),
    ('pt-br', u'Português')
]

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, '../locale'),
)

MEDIA_ROOT = os.path.join(PROJECT_PATH, '../tmp/')

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Amazon AWS S3
AMAZON_AWS = {
    'AWS_ACCESS_KEY_ID': 'xxx',
    'AWS_SECRET_ACCESS_KEY': 'xxx',
    'S3_BUCKET': 'xxx'
}
