from pathlib import Path
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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': 5432,
    }
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
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party libs
    "rest_framework",
    "apps.core",
)

AUTH_USER_MODEL = "core.User"