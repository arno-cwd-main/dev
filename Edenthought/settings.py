
from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'django-insecure-9vqe(1+jysq&fhrdom!tcl%m34df=*6f12v)8_&kc=5y04i=%%'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False # - TURN OFF IN PRODUCTION!

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'journal.apps.JournalConfig',

    'crispy_forms',

    'storages',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Edenthought.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Edenthought.wsgi.application'


# Databases

# - Database configuration (SQL-LITE) --------------------------------------------# 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# - Database configuration (PostgreSQL) --------------------------------------------# 

'''

DATABASES = {

    'default': {
        
        'ENGINE': 'django.db.backends.postgresql',
        
        'NAME': '',
    
        'USER' : '',

        'PASSWORD' : '', 

        'HOST' : '',

        'PORT' : '5432',

    }

}

'''


# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'

MEDIA_URL = 'images/'


STATICFILES_DIRS = [ BASE_DIR / 'static']

MEDIA_ROOT = BASE_DIR / 'static/images'


# - Heroku will run and collect our static files

#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # - Uncomment when deploying to heroku



# - SMTP configuration --------------------------------------------# 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = 'True'

EMAIL_HOST_USER = '********' # - GMAIL email address
EMAIL_HOST_PASSWORD = '********' # - APP password

DEFAULT_FROM_EMAIL = '********' # - GMAIL email address


# - S3 buckets configuration --------------------------------------------# 

'''
# - Access key (IMPORTANT - STORE AS ENVIRONMENT VARIABLES)

AWS_ACCESS_KEY_ID = "********" 

# - Secret access key (IMPORTANT - STORE AS ENVIRONMENT VARIABLES)

AWS_SECRET_ACCESS_KEY = "********" 


AWS_STORAGE_BUCKET_NAME = "" # - Enter your bucket name

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
'''








