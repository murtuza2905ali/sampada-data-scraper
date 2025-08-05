import os
from pathlib import Path
import dj_database_url   # make sure this is in requirements.txt

BASE_DIR = Path(__file__).resolve().parent.parent

# Pull SECRET_KEY from env (fall back to your local-only default)
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-very-secret-key"  # local-dev fallback only
)

# DEBUG = False in production; default to True only if the ENV var is missing
DEBUG = os.environ.get("DEBUG", "True").lower() in ("1", "true", "yes")

# ALLOWED_HOSTS must include your Render app domain(s)
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",          # for static files
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myapp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # serve static
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sampada_scraper.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "myapp/templates"],
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

WSGI_APPLICATION = "sampada_scraper.wsgi.application"

# Database: use Postgres if DATABASE_URL is set, else SQLite for local
if os.environ.get("DATABASE_URL"):
    DATABASES = {
        "default": dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Tesseract OCR path from env (fallback only for local)
TESSERACT_PATH = os.environ.get("TESSERACT_PATH", "/usr/bin/tesseract")

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

# Static files config
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
