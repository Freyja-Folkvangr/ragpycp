"""
Django settings for ragcp project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import logging

from ragcp.utils import get_configuration, get_rss_address

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

logger = logging.getLogger(__name__)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&h74#_%&b)k9x$xobgi!c7jq)v$l^$#go#26ng!bbc@_y8pofq'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'freyja-ragcp.herokuapp.com']

try:
    host = get_configuration('HOST')
except Exception:
    host = None
    pass

if host:
    ALLOWED_HOSTS.append(host)
    if host in ['127.0.0.1', 'localhost'] or '.local' in host:
        DEBUG = True
    else:
        DEBUG = True
else:
    DEBUG = True
logger.info('The HOST is %s and debug is %s' % (host, DEBUG))

# Application definition

INSTALLED_APPS = [
    'ragcp.apps.RagcpConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.humanize',
    'users',
    'char',
    'mathfilters',
    'servicedesk',
    'content',
    'thor'
]

AUTH_USER_MODEL = 'users.Login'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ragcp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'ragcp.wsgi.application'

try:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': get_configuration('DATABASE_NAME'),
            'USER': get_configuration('DATABASE_USER'),
            'PASSWORD': get_configuration('DATABASE_PASSWORD'),
            # 'PASSWORD': '7DtMAZ5YHEUpkq5j',
            'HOST': get_configuration('DATABASE_HOST'),
            'PORT': get_configuration('DATABASE_PORT'),
            'OPTIONS': {
                # 'init_command': 'SET storage_engine=InnoDB', #For MySQL 5.6
                'init_command': 'SET default_storage_engine=INNODB', #For MySQL 5.7+
                'charset': 'utf8mb4' # to support emoji in posts
                # better to set this in your database config, otherwise django has to do a query everytime
            }
        }
    }
except KeyError as err:
    logger.error('Could not load one or more database settings from environment variables.')
    logger.error(err)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
]

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Report bugs to Freyja-Folkvangr to get them fixed
sentry_sdk.init(
    dsn="https://5dffbd4c49cf429ca58a0b8e4186ffb9@o541391.ingest.sentry.io/5660228",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)


# Features configured through environment variables
FEED_ADDRESS = get_rss_address()

# User settings
FEED_ENABLED = True
