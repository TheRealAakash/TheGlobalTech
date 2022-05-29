"""
Django settings for EnvironmentML project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# REALLY BAD METHOD
import django
from django.utils.encoding import force_str

django.utils.encoding.force_text = force_str
# TILL HERE
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e*1$oedz8$s*!7!0h+_5c2sb)2@a!j2wnn4n617-=92heo5^gg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# CHANGE THIS
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_webp',

    'main.apps.MainConfig',
    # added
    "tinymce",
    "jquery",
    'django_select2',
    # all auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.apple',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    # end allauth
    # wagtail
    'wagtailfontawesome',
    "wagtail.contrib.table_block",
    'wagtail.contrib.sitemaps',
    'wagtail.contrib.routable_page',
    'django_social_share',
    'wagtailcodeblock',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail_content_import',
    'wagtail_content_import.pickers.google',
    'wagtail_content_import.pickers.local',
    'wagtail.admin',
    'wagtail.core',
    'modelcluster',
    'taggit',

    'colorful',
    # end wagtail
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # wagtail
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'EnvironmentML.urls'

TEMPLATES = [
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
                'django_webp.context_processors.webp',
            ],
        },
    },
]

WSGI_APPLICATION = 'EnvironmentML.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'EnvironmentML',
        'USER': 'EnvironmentML',
        'PASSWORD': '83247923847923749',
        'HOST': '192.168.1.3',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

CACHES = {
    # … default cache config and others
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SELECT2_CACHE_BACKEND = "default"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

# allauth
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
# end allauth

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_ROOT = "media/"
STATICFILES_DIRS = []

# wagtail
WAGTAIL_SITE_NAME = 'The Global Tech'
TAGGIT_CASE_INSENSITIVE = True
# Replace the search backend
# WAGTAILSEARCH_BACKENDS = {
#  'default': {
#    'BACKEND': 'wagtail.search.backends.elasticsearch5',
#    'INDEX': 'myapp'
#  }
# }

# Wagtail email notifications from address
# WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = 'wagtail@myhost.io'

# Wagtail email notification format
# WAGTAILADMIN_NOTIFICATION_USE_HTML = True

PUPUT_AS_PLUGIN = True
WAGTAILCONTENTIMPORT_GOOGLE_PICKER_API_KEY = "AIzaSyDRWVI29R3GAHC2-4ohConiy4gNR19f06Q"
WAGTAILCONTENTIMPORT_GOOGLE_OAUTH_CLIENT_CONFIG = '{"web":{"client_id":"143649260242-lm9g7net7n84s9uqhnrrgl9qkpbi4soa.apps.googleusercontent.com","project_id":"the-global-tech","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"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","redirect_uris":["https://theglobaltech.org"],"javascript_origins":["https://theglobaltech.org"]}}'
WAGTAIL_CODE_BLOCK_LINE_NUMBERS = True
WAGTAIL_CODE_BLOCK_THEME = 'okaidia'
WAGTAILEMBEDS_RESPONSIVE_HTML = True
# auth
SOCIALACCOUNT_PROVIDERS = {
    "github": {
        # For each provider, you can choose whether or not the
        # email address(es) retrieved from the provider are to be
        # interpreted as verified.
        "VERIFIED_EMAIL": True
    },
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APP": {
            "client_id": "143649260242-lm9g7net7n84s9uqhnrrgl9qkpbi4soa.apps.googleusercontent.com",
            "secret": "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",
            "key": "AIzaSyBIw_uanFCGfkxhLRuaPTtAPFkXry74C3I"
        },
        # These are provider-specific settings that can only be
        # listed here:
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    }
}

SITE_ID = 1

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USERNAME_BLACKLIST = ['admin', 'root']
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_USERNAME_MIN_LENGTH = 3

WAGTAILIMAGES_MAX_UPLOAD_SIZE = 20 * 1024 * 1024
# smtp
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = "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"
DEFAULT_FROM_EMAIL = 'no-reply@theglobaltech.org'
