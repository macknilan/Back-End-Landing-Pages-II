"""
Django settings for landingpage project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['MUEBLERIALLAVE']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '52.8.45.246', 'muebleria.konetl.co']
# ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'landingpage',
    'categorias',
    'muebles',
    'ckeditor',
    'django_extensions',
    'storages',
    'sorl.thumbnail',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',  # ESTO PARA USAR CACHING PERO EN PRODUCCION EN LA 1ra LINEA
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',  # ESTO PARA USAR CACHING PERO EN PRODUCCION EN LA ULTIMA LINEA
)

ROOT_URLCONF = 'landingpage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # SE LE DICE A DJANGO QUE BUSQUE LA CARPETA templates
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates'), ],
        # SE LE DICE A DJANGO QUE EN CADA APP BUSQUE LA CARPETA templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # LISTA DE MUEBLES RELACIONADOS COMO LINKS EN INFERIOR DE PAGINA
                'landingpage.context_processors.lista_link_muebles_relacionados',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'landingpage.wsgi.application'


# ################ DATABASE ################
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['MUEBLERIANAME'],
        'USER': os.environ['MUEBLERIAUSER'],
        'PASSWORD': os.environ['MUEBLERIAPASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}
# ################ MEMCACHED ################
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
# ################ MEMCACHED ################
# ################ REDIS ################
# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.RedisCache',
#         'LOCATION': '127.0.0.1:6379',
#         'OPTIONS': {
#             'DB': 1,
#             #  'PASSWORD': '',
#             'PARSER_CLASS': 'redis.connection.HiredisParser'
#         }
#     }
# }
# 
# THUMBNAIL_REDIS_HOST = 'localhost'
# THUMBNAIL_REDIS_PORT = 6379
# ################ REDIS ################

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# ################ DATABASE ################

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ############################################ STATIC & MEDIA FIELDS ############################################
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

if DEBUG:
    STATIC_URL = '/static/'

    STATIC_ROOT = os.sep.join(
        os.path.abspath(__file__).split(os.sep)[:-2] + ['static'])

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'landingpage/static'),
    )

    STATICFILES_FINDERS = (
        # BUSCA LOS ARCHIVOS ESTATICOS EN EL SISTEMA DE ARCHIVOS
        'django.contrib.staticfiles.finders.FileSystemFinder',
        # BUSCA LOS ARCHIVOS ESTATICOS EN LA CARPETAS DE LAS APLICACIONES
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    # PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION DEBUG = False
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
    # PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION

    MEDIA_URL = '/media/'
#    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_ROOT = os.sep.join(
        os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])


# ###################### AWS S3 SETTINGS ######################
# ############ CKEDITOR ############
# AWS_QUERYSTRING_AUTH = False
# CKEDITOR_UPLOAD_PATH = "uploads_by_ckeditor/"
# ############ CKEDITOR ############
if DEBUG is False:

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'landingpage/static'),
    )

    STATICFILES_FINDERS = (
        # BUSCA LOS ARCHIVOS ESTATICOS EN EL SISTEMA DE ARCHIVOS
        'django.contrib.staticfiles.finders.FileSystemFinder',
        # BUSCA LOS ARCHIVOS ESTATICOS EN LA CARPETAS DE LAS APLICACIONES
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
    AWS_STORAGE_BUCKET_NAME = 'muebleria'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    STATICFILES_LOCATION = 'static'
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'

    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

# ###################### AWS S3 SETTINGS ######################
# ############################################ STATIC & MEDIA FIELDS ############################################

# ################## CKEDITOR ##################
CKEDITOR_UPLOAD_PATH = "uploads_by_ckeditor/"
# ################## CKEDITOR ##################
# ######################## SEND EMAILS ########################
EMAIL_USE_TLS = True
"""EMAIL_HOST = 'EMAIL_HOST'"""
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
"""EMAIL_HOST_USER = 'EMAIL_HOST_USER'"""
EMAIL_HOST_USER = 'nomackayu@gmail.com'
"""EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'"""
EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
# ######################## SEND EMAILS ########################
# ###################### DJANGO-CKEDITOR ######################
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'UltraFull',
        'height': 300,
        'toolbar_UltraFull': [
            ['Source', '-', 'Save', 'NewPage', 'DocProps', 'Preview', 'Print', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Find', 'Replace', '-', 'SelectAll', '-', 'SpellChecker', 'Scayt'],
#            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks', '-', 'About'],
        ],
        'forcePasteAsPlainText': True,
    },
}
# ###################### DJANGO-CKEDITOR ######################

