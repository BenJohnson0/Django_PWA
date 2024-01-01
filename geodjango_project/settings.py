
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

GDAL_LIBRARY_PATH = r'C:\OSGEO4W\bin\gdal307.dll'
GEOS_LIBRARY_PATH = r'C:\OSGeo4W\bin\geos_c.dll'

#GDAL_LIBRARY_PATH = '/usr/lib/libgdal.so'
#GEOS_LIBRARY_PATH = '/usr/lib/libgeos_c.so'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e6w$+=o8=6pn*8&ojveqo-1oa!9zbl%p1_q*4us3c(lbzbd1y2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.gis',
    'geodjangoPWA_app',
    'rest_framework',
    'pwa',
    'leaflet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'geodjango_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'geodjangoPWA_app/templates'],
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

WSGI_APPLICATION = 'geodjango_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',

        # local definition
        'NAME': 'postgres',
        'HOST': 'localhost',
        'USER': 'docker',
        'PASSWORD': 'docker',
        'PORT': 25432

        # container definition
        #'NAME': 'postgres',
        #'HOST': 'localhost',
        #'USER': 'docker',
        #'PASSWORD': 'docker',
        #'PORT': 25432
    }
}

LEAFLET_CONFIG = {
    # "SPATIAL_EXTENT": (5.0, 44.0, 7.5, 46),
    "DEFAULT_CENTER": (53.0, -8),
    "DEFAULT_ZOOM": 7,
    "MIN_ZOOM": 3,
    "MAX_ZOOM": 13,
    "DEFAULT_PRECISION": 6,
    "SCALE": "both",
    "ATTRIBUTION_PREFIX": "powered by Ben Johnson",
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'geodjangoPWA_app/static/'),
]

STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '/static/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'geodjangoPWA_app/static/serviceworker.js')

PWA_APP_NAME = 'Ben\'s App'
PWA_APP_DESCRIPTION = 'PWA App Description'
PWA_APP_THEME_COLOR = '#61a85e'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'

