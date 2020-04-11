# -*- coding: utf-8 -*-

"""
Django settings for pizzapp project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
NAME = 'NAME'
dname = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(dname)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^)phcn9ojmovleo5@y^doedr1t55-wy3-=9h9aws!d*xelt*az'   # noqa: S105

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['testserver']  # noqa: WPS407


# Application definition

INSTALLED_APPS = [  # noqa: WPS407
    'pizzapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nazrpizza',
]

MIDDLEWARE = [  # noqa: WPS407
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pizzapp.urls'

TEMPLATES = [   # noqa: WPS407
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

WSGI_APPLICATION = 'pizzapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {  # noqa: WPS407
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        NAME: os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

P_VALIDATION = 'django.contrib.auth.password_validation'

AUTH_PASSWORD_VALIDATORS = [    # noqa: WPS407
    {
        NAME:
            '{0}.UserAttributeSimilarityValidator'.format(P_VALIDATION),
    },
    {
        NAME:
            '{0}.MinimumLengthValidator'.format(P_VALIDATION),
    },
    {
        NAME:
            '{0}.CommonPasswordValidator'.format(P_VALIDATION),
    },
    {
        NAME:
            '{0}.NumericPasswordValidator'.format(P_VALIDATION),
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


# SMTP settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

EMAIL_HOST_USER = 'mozgolom1999991@gmail.com'
EMAIL_HOST_PASSWORD = 'o0c8v7setye56s'  # noqa: S105

DEFAULT_FROM_EMAIL = 'mozgolom1999991@gmail.com'
SERVER_EMAIL = 'mozgolom1999991@gmail.com'
