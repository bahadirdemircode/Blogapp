"""
Django settings for blogapp project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from os import getenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-6d1_z9236#webyq^rhug!v0w^6%2cup&jxsq&ir!p$e!hczog'
#SECRET_KEY = 'django-insecure-_z1mh$duegv8sq#n9metrwk=b=85s0#%1@^g)n&9j=13houq7='
SECRET_KEY = 'niqqf=ju_3a0iv4z(u3vhk=6zt*y_g#2ax*)%-yqe2oi)5ze^6'
#SECRET_KEY = getenv("SECRET_KEY")
#SECRET_KEY = getenv("SECRET_KEY", 'django-insecure-default') 


#SECRET_KEY = os.getenv("SECRET_KEY", "default-value-if-missing")
SECRET_KEY = getenv("SECRET_KEY", "default-fallback-key")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = getenv("IS_DEVELOPMENT", True)

#ALLOWED_HOSTS = [ getenv("APP_HOST")]

#ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
#ALLOWED_HOSTS = ['.elasticbeanstalk.com', 'localhost', '127.0.0.1']
DEBUG = os.getenv("DEBUG", "False") == "True"
#ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", ".elasticbeanstalk.com").split(",")
#ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']
ALLOWED_HOSTS = ["django-blogapp-yedek.onrender.com", "127.0.0.1"]

#ALLOWED_HOSTS = ['.elasticbeanstalk.com']



# Application definition

INSTALLED_APPS = [
    'blogapp',  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.tz',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Deployment için
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/homework/list/'
LOGOUT_REDIRECT_URL = '/'


