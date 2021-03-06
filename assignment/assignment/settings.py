"""
Django settings for assignment project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!%l_6x0=6)p1xgb*!#011d5cg)#wr-_uhz7vn5&7bj%b(&1yvs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

"""
configure ALLOWED_HOSTS to allow multiple hosts (don't do that in production!):
test cases at cmd: 
1. curl -v -H "Host:www.example-A.com" http://127.0.0.1:8000/
1. curl -v -H "Host:www.example-B.com" http://127.0.0.1:8000/
1. curl -v -H "Host:www.example-C.com" http://127.0.0.1:8000/
1. curl -v -H "Host:www.example-D.com" http://127.0.0.1:8000/
1. curl -v -H "Host:www.example-E.com" http://127.0.0.1:8000/

"""

ALLOWED_HOSTS = ["example-A.com", 'www.example-B.com','www.example-C.com','127.0.0.1'] # allowed only for these 
# ALLOWED_HOSTS = ["*"] # for all

REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework_api_key.permissions.HasAPIKey', # The HasAPIKey permission class protects a view behind API key authorization
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',

    ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.TokenAuthentication',
    # )

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'authapp.backends.JWTAuthentication',
    #     'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    )
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_api_key',# Add the API Key app then apply migrations using migrate command in terminal
    'django_filters',
    'rest_framework.authtoken',
    'authapp.apps.AuthappConfig',
    'django_extensions',
    'corsheaders',
    # 'authemail',
    # 'rest_registration',
    'promantus.apps.PromantusConfig',
    'accounts.apps.AccountsConfig',

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

ROOT_URLCONF = 'assignment.urls'
# AUTH_USER_MODEL = 'accounts.MyUser'
CORS_ORIGIN_ALLOW_ALL= True
# SESSION_ENGINE = 'redis_sessions.session'
# Access-Control-Allow-Origin = 
# Access-Control-Allow-Credentials : True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'from_email@gmail.com'
EMAIL_HOST_PASSWORD = "********"
EMAIL_PORT = 587, 


# LOGIN_REDIRECT_URL = "userinfo"
# LOGOUT_REDIRECT_URL = ""

# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'from_email@gmail.com'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/templates/',
        ],
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

WSGI_APPLICATION = 'assignment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test1',
        'USER': 'postgres',
        'PASSWORD': 'promantus',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

"""--------RSA Key Generator for Public and Private key------------------"""
from Crypto.PublicKey import RSA

RSAkey = RSA.generate(1024)

# JWT
# JWT_SECRET_KEY = "JWT_SECRET_KEYJWT_SECRET_KEYJWT_SECRET_KEYJWT_SECRET_KEY"
JWT_SECRET_KEY = {
        "private_key":RSAkey.exportKey(),
        "public_key": RSAkey.publickey().exportKey()
    }

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

"""set the API_KEY_CUSTOM_HEADER setting to a non-None value to require clients to pass 
their API key in a custom header instead of the Authorization header."""

API_KEY_CUSTOM_HEADER = None

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
