import os
from pathlib import Path

from dotenv import load_dotenv

from celery import Celery
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", default="")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG", default=True)

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # apps
    "users.apps.UsersConfig",
    "consultation.apps.ConsultationConfig",
    "telegram_bot",
    # installs
    "rest_framework",
    "aiogram",
    "django_celery_results",
    "pytest",
    "pytest_django",
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

# REST FRAMEWORK
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
DEFAULT_TIME_FORMAT = "%H:%M"
DEFAULT_DATETIME_FORMAT = f"{DEFAULT_DATE_FORMAT}T{DEFAULT_TIME_FORMAT}"
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "TIME_FORMAT": DEFAULT_TIME_FORMAT,
    "TIME_INPUT_FORMATS": [DEFAULT_TIME_FORMAT],
    "DATE_FORMAT": DEFAULT_DATE_FORMAT,
    "DATE_INPUT_FORMATS": [DEFAULT_DATE_FORMAT],
    "DATETIME_FORMAT": DEFAULT_DATETIME_FORMAT,
    "DATETIME_INPUT_FORMATS": [DEFAULT_DATETIME_FORMAT],
}

ROOT_URLCONF = "sumeet_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "sumeet_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", default="sumeet_db"),
        "USER": os.getenv("POSTGRES_USER", default="postgres_user"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", default="postgres_password"),
        "HOST": os.getenv("POSTGRES_HOST", default="localhost"),
        "PORT": os.getenv("POSTGRES_PORT", default=5432),
    },
}


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
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")

MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles/")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

# telegram
TELEGRAM_BOT_NAME = os.getenv("TELEGRAM_BOT_NAME", default="")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", default="")

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# Настройки для Celery

CELERY_TIMEZONE = "Asia/Bishkek"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

CELERY_BROKER_URL = f'redis://:{os.getenv("REDIS_PASSWORD", default="")}@redis:6379'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

# Test
