import os
import qrtrack
DEVELOPMENT_SETTINGS_VERSION = 'alpha'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'qrtrack.core',
    'qrtrack.qrcodes',
    'qrtrack.analytics',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'qrtrack.core.middleware.ForceDefaultLanguageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

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
                'qrtrack.core.context_processors.core_processor',
            ],
        },
    },
]

LANGUAGES = (
    ('en', 'English'),
    ('pl', 'Polish'),
)

LOCALE_PATHS = [
    os.path.join(os.path.dirname(qrtrack.__file__), 'locale'),
]

ROOT_URLCONF = 'qrtrack.deployment.urls'

WSGI_APPLICATION = 'wsgi.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/'

# So we can track the user ALWAYS, even if no qrcode found
SESSION_SAVE_EVERY_REQUEST = True
