"""
Django settings for qrtrack project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from qrtrack.deployment.core_settings import *

# If your deployment will have an older version of settings.py the server won't start
# You'll have to check qrtrack.deployment.skeleton.settings.py for differences and then update below
# variable
DEPLOYED_SETTINGS_VERSION = '__SETTINGS_VERSION__'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONTACT_EMAIL = 'some@email.com'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    #'qrtrack.mimuw',
) + INSTALLED_APPS

MIDDLEWARE_CLASSES = (
) + MIDDLEWARE_CLASSES

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',  # sqlite3; postgresql_psycopg2
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': ''
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'  # supported en; pl

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# You probably don't need (or shouldn't) touch the settings below

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '__SECRET_KEY__'
COLLECT_ID_SALT = '__COLLECT_SALT__'
SHOW_ID_SALT = '__SHOW_SALT__'

STATIC_ROOT = '__STATIC_ROOT__'
MEDIA_ROOT = '__MEDIA_ROOT__'
