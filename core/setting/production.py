from core.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v9uc0)%dq@9%l)c2tb^*)a5cv$14u)tgojy^gcsetymkanmj+v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

SITE_ID = 2

# INSTALLED_APPS = []

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

# CSRF_COOKIE_SECURE = True
