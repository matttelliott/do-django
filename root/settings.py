"""
Django settings for root project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from os import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-8pd&v)44$yxw0mk8yt9%7bvtkn04obke^ggz#)jom#9lwhpvm!",
)



HOSTNAME = environ.get("HOSTNAME")
APP_URL = environ.get("APP_URL")

DATABASE_HOST = environ.get("DATABASE_HOST")
DATABASE_PORT = environ.get("DATABASE_PORT")
DATABASE_NAME = environ.get("DATABASE_NAME")
DATABASE_USER = environ.get("DATABASE_USER")
DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD")

AWS_ACCESS_KEY_ID = environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = environ.get("AWS_S3_ENDPOINT_URL")
AWS_LOCATION = environ.get("AWS_LOCATION", 'static')

print(AWS_ACCESS_KEY_ID)
print(AWS_SECRET_ACCESS_KEY)
print(AWS_STORAGE_BUCKET_NAME)
print(AWS_S3_ENDPOINT_URL)
print(AWS_LOCATION)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if HOSTNAME:
    ALLOWED_HOSTS = [HOSTNAME]

if APP_URL:
    CSRF_TRUSTED_ORIGINS = [APP_URL]



# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "schema",
    'rest_framework',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "root.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "root.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = (
    {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DATABASE_NAME,
            "USER": DATABASE_USER,
            "PASSWORD": DATABASE_PASSWORD,
            "HOST": DATABASE_HOST,
            "PORT": DATABASE_PORT,
        }
    }
    if DATABASE_NAME
    and DATABASE_USER
    and DATABASE_PORT
    and DATABASE_PASSWORD
    and DATABASE_HOST
    else {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
)


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
MEDIA_URL = "media/"
MEDIA_ROOT = "media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

if (
    AWS_ACCESS_KEY_ID
    and AWS_SECRET_ACCESS_KEY
    and AWS_STORAGE_BUCKET_NAME
    and AWS_S3_ENDPOINT_URL
):
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {},
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {},
        },
    }
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_S3_SIGNATURE_VERSION = "v4"


STATICFILES_DIRS = []
MEDIA_ROOT = "media/"
MEDIA_URL = "media/"


STATIC_URL = (
    "https://%s/%s/" % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
    if AWS_S3_ENDPOINT_URL and AWS_LOCATION
    else "static/"
)



REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
