import os
from datetime import timedelta
from pathlib import Path

import django_heroku
from prettyconf import config

from utils.settings import get_project_package

# Project Structure
BASE_DIR = Path(__file__).absolute().parents[2]
PROJECT_DIR = Path(__file__).absolute().parents[1]
FRONTEND_DIR = PROJECT_DIR / "frontend"
SECRET_KEY = config("SECRET_KEY", default="")

# Debug & Development
DEBUG = config("DEBUG", default=False, cast=config.boolean)

# Database
# Database
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": os.path.join(BASE_DIR, "db.sqlite3")}
}


# Miscelaneous
_project_package = get_project_package(PROJECT_DIR)
ROOT_URLCONF = f"{_project_package}.urls"
WSGI_APPLICATION = f"{_project_package}.wsgi.application"
LOG_REQUEST_ID_HEADER = "HTTP_X_REQUEST_ID"

# Media & Static
MEDIA_URL = "/media/"
STATIC_URL = "/static/"
STATIC_ROOT = FRONTEND_DIR / "static"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(FRONTEND_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": config("TEMPLATE_DEBUG", default=DEBUG, cast=config.boolean),
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

# Application
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party libs
    "rest_framework",
    "apps.core",
    "corsheaders",
)

# Rest Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
}

CSRF_COOKIE_SECURE = True

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=config("ACCESS_TOKEN_LIFETIME", cast=int)),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=config("REFRESH_TOKEN_LIFETIME", cast=int)),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUTH_HEADER_TYPES": ("JWT",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "JWT",
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

django_heroku.settings(locals())


CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", cast=config.list)

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
