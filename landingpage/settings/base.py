import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'categorias',
    'muebles',
    'ckeditor',
    'sorl.thumbnail',
    'captcha',
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
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'landingpage.context_processors.lista_link_muebles_relacionados',
                'landingpage.context_processors.FooterMiniGalery',
            ],
        },
    },
]


WSGI_APPLICATION = 'landingpage.wsgi.application'

# #--------------# DATABASE #--------------#
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

# #--------------# MEMCACHED #--------------#
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
# #--------------# MEMCACHED #--------------#
# #----------------# REDIS #----------------#
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
# #----------------# REDIS #----------------#

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# #--------------# DATABASE #--------------#

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# #----------------------# SEND EMAILS #----------------------#
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

# #----------------------# SEND EMAILS #----------------------#
# #--------------------# DJANGO-CKEDITOR #--------------------#
CKEDITOR_UPLOAD_PATH = "uploads_by_ckeditor/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Classic',
        'height': 200,
        'width': 600,
        'toolbar_Classic': [
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Scayt'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['Maximize'],
            ['Source'],
            '/',
            ['Bold', 'Italic', 'Strike', '-', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote'],
            ['Styles', 'Format'],
            ['About'],
        ],
    },
}
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'UltraFull',
#         'height': 300,
#         'toolbar_UltraFull': [
#             ['Source', '-', 'Save', 'NewPage', 'DocProps', 'Preview', 'Print', '-', 'Templates'],
#             ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
#             ['Find', 'Replace', '-', 'SelectAll', '-', 'SpellChecker', 'Scayt'],
# #            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
#             ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
#             ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
#                 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl'],
#             ['Link', 'Unlink', 'Anchor'],
#             ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
#             ['Styles', 'Format', 'Font', 'FontSize'],
#             ['TextColor', 'BGColor'],
#             ['Maximize', 'ShowBlocks', '-', 'About'],
#         ],
#         'forcePasteAsPlainText': True,
#     },
# }
# #--------------------# DJANGO-CKEDITOR #--------------------#
#

RECAPTCHA_PRIVATE_KEY = '6LcG9xcTAAAAAJ93QLbpLZc-IoG2AXNvc8ZesLk9'
RECAPTCHA_PUBLIC_KEY = '6LcG9xcTAAAAAO2tq6gGcqQ4hXszuSSW_Ynfdrz-'
NOCAPTCHA = True
RECAPTCHA_USE_SSL = True
