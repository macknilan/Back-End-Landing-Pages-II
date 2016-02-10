#
from .base import *

SECRET_KEY = os.environ['MUEBLERIALLAVE']

DEBUG = False

ALLOWED_HOSTS = ['.rodolfougalde.xyz']

INSTALLED_APPS += (
    'storages',
)

# #----------# CKEDITOR #----------#
AWS_QUERYSTRING_AUTH = False
# #----------# CKEDITOR #----------#

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

