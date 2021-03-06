import os

ROOT = os.path.dirname(os.path.realpath(__file__))

ADMINS = (
    ('Charly', 'chack14rock@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(ROOT, '../..', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(ROOT, '../..', 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(ROOT, '../..', 'assets'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '6s8oc&r7kl!dwy96q8v26%k-rty=$8)&-7ym6zc9u)dfimu^8!'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'udon.urls'

WSGI_APPLICATION = 'udon.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(ROOT, '../..', 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'south',
    'library',
    'adminpanel',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
