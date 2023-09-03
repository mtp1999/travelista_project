from core.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n4hz7k9$z^)=w$z10t7v6dke_4nyq&hvye4qgs@zt4wn1@7uz!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INTERNAL_IPS = [
    "127.0.0.1",
]

# sites
SITE_ID = 2


STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

COMPRESS_ENABLED = True
COMPRESS_ROOT = BASE_DIR / 'compress_static'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]