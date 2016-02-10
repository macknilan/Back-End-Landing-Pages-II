#
from .base import *

SECRET_KEY = os.environ['MUEBLERIALLAVE']

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += (
    'django_extensions',

)

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
# ######################## STATIC & MEDIA FIELDS ########################

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "COLLECT_STATIC", "static_root")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "COLLECT_STATIC", "media_root")
# ######################## STATIC & MEDIA FIELDS ########################
# #----------------------# SEND EMAILS #----------------------#
EMAIL_USE_TLS = True
EMAIL_HOST = 'EMAIL_HOST'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'EMAIL_HOST_USER'
EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
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


