"""
Django settings.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
#from dotenv import load_dotenv, find_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "accounts", "templates")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "2093d84709q274uikfja793w84uaiozds8723i"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

USE_X_FORWARDED_HOST = True
ALLOWED_HOSTS = [
    "makers.eapl.me",
    "localhost",
    "127.0.0.1",
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "mptt",
    "debug_toolbar",
    "accounts",
    "news",
    "emaildigest",
    "magiclink",
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'django.middleware.gzip.GZipMiddleware',
    #'htmlmin.middleware.HtmlMinifyMiddleware', # TODO: When activated, Django Debug Toolbar has JS issues
    "htmlmin.middleware.MarkRequestMiddleware",
]

ROOT_URLCONF = "notes.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "notes.context_processors.settings_context_processor",
            ],
        },
    },
]

WSGI_APPLICATION = "notes.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

AUTHENTICATION_BACKENDS = (
    "magiclink.backends.MagicLinkBackend",
    "django.contrib.auth.backends.ModelBackend",
)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = "es"
TIME_ZONE = "UTC"

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = "/var/www/news.gemugami.com/static/"

AUTH_USER_MODEL = "accounts.CustomUser"

INTERNAL_IPS = [
    "127.0.0.1",
]

PAGING_SIZE = 30
HTML_MINIFY = True

LOGOUT_REDIRECT_URL = "/"
LOGIN_REDIRECT_URL = "/"

ACCEPT_UNINVITED_REGISTRATIONS = True

SITE_NAME = "Notas Makers"
SITE_URL = "https://makers.eapl.me"
SITE_DOMAIN = "makers.eapl.me"

# Set Djangos login URL to the magiclink login page
LOGIN_URL = "magiclink:login"

MAGICLINK_LOGIN_TEMPLATE_NAME = "accounts/login.html"
MAGICLINK_LOGIN_SENT_TEMPLATE_NAME = "accounts/login_sent.html"
MAGICLINK_LOGIN_FAILED_TEMPLATE_NAME = "accounts/login_failed.html"

MAGICLINK_REQUIRE_SIGNUP = True
MAGICLINK_SIGNUP_TEMPLATE_NAME = "accounts/register.html"
# MAGICLINK_SIGNUP_TEMPLATE_NAME = 'accounts/signup.html'

MAGICLINK_EMAIL_TEMPLATE_NAME_TEXT = "accounts/login-email.txt"
MAGICLINK_EMAIL_TEMPLATE_NAME_HTML = "accounts/login-email.html"

MAGICLINK_EMAIL_STYLES = {
    'logo_url': 'http://127.0.0.1:8000/static/icon.png',
    "background-colour": "#ffffff",
    "main-text-color": "#000000",
    "button-background-color": "#0078be",
    "button-text-color": "#ffffff",
}

MAGICLINK_TOKEN_LENGTH = 64
MAGICLINK_REQUIRE_SAME_BROWSER = False

# Save credentials in another .env file
# https://stackoverflow.com/a/61437799
# Sending email
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER =
EMAIL_HOST_PASSWORD =
