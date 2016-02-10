#
from .base import *

SECRET_KEY = os.environ['MUEBLERIALLAVE']

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += (
    'django_extensions',

)


# ######################## STATIC & MEDIA FIELDS ####################### #

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "COLLECT_STATIC", "static_root")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "COLLECT_STATIC", "media_root")

# ######################## STATIC & MEDIA FIELDS ####################### #


