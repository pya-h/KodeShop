from pathlib import Path
from django.contrib.messages import constants as messages
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

# for normal debug:
# DEBUG = True
# ALLOWED_HOSTS = []

# for heroku app:
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # thirdparty apps:
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'robots.apps.RobotsConfig',
    'admin_honeypot',
    'django_ckeditor_5',
    # my apps
    'category',
    'post',
    'user',
    'store',
    'stack',
    'purchase',
    'dashboard',
    'messaging',
    # 'gateways'
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]
# implement auto logout in case in activity for specific eriod of time
SESSION_EXPIRE_SECONDS = 7200  # 1 hour
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_TIMEOUT_REDIRECT = 'user/login'

ROOT_URLCONF = 'kodeshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processor.list_categories',
                'stack.context_processor.stack_counter'
            ],
        },
    },
]

WSGI_APPLICATION = 'kodeshop.wsgi.application'

AUTH_USER_MODEL = 'user.User'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', 'user.utilities.UserLoginBackend',)
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': BASE_DIR / config('DB_NAME'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = config('LANGUAGE_CODE')

TIME_ZONE = config('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    50: 'critical'
}

# email - SMTP configuration :
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default="localhost")
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)  # port for gmail
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_APP_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
# EMAIL_USE_SSL = config('EMAIL_USE_SSL', cast=bool)


# Robots config
ROBOTS_USE_SITEMAP = True
ROBOTS_USE_HOST = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    'kodeshop/static',
]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static'
# USE_THOUSAND_SEPARATOR = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|', 'bold', 'italic', 'underline', 'strikethrough', 'link',
            'alignment', 'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'highlight',
            'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', 'insertTable',
            'insertVideo', 'mediaEmbed', '|', 'undo', 'redo'
        ],
        'height': '100%',
        'width': '100%',
        'fontFamily': {
            'options': [
                'default',
                'Arial, sans-serif',
                'Courier New, Courier, monospace',
                'Georgia, serif',
                'Times New Roman, Times, serif',
                'Verdana, Geneva, sans-serif'
            ],
            'supportAllValues': True
        },
        'fontSize': {
            'options': [
                'default',
                '8px', '10px', '12px', '14px', '16px', '18px', '20px', '24px', '28px', '32px', '36px'
            ],
            'supportAllValues': True
        },
        'fontColor': {
            'columns': 5,
            'colors': [
                {'color': 'rgb(0, 0, 0)', 'label': 'Black'},
                {'color': 'hsl(0, 75%, 60%)', 'label': 'Red'},
                {'color': 'hsl(30, 75%, 60%)', 'label': 'Orange'},
                {'color': 'rgb(255, 255, 255)', 'label': 'White'},
                {'color': 'rgb(0, 255, 0)', 'label': 'Green'},
                {'color': 'rgb(0, 0, 255)', 'label': 'Blue'},
            ]
        },
        'highlight': {
            'options': [
                {'model': 'yellowMarker', 'class': 'marker-yellow', 'title': 'Yellow Marker',
                 'color': 'var(--ck-highlight-marker-yellow)'},
                {'model': 'greenMarker', 'class': 'marker-green', 'title': 'Green Marker',
                 'color': 'var(--ck-highlight-marker-green)'},
                {'model': 'blueMarker', 'class': 'marker-blue', 'title': 'Blue Marker',
                 'color': 'var(--ck-highlight-marker-blue)'},
            ]
        },
        'mediaEmbed': {
            'previewsInData': True,
            'uploadUrl': '/ckeditor5/upload-video/',
            'providers': [
                'youtube.com', 'vimeo', 'dailymotion', 'twitch', 'facebook', 'instagram'
            ]
        },
        # 'extraPlugins': ','.join([
        #     'uploadimage',  # Image upload support
        #     'font',         # Font styling options
        #     'alignment',    # Text alignment options
        #     'highlight',    # Text highlighting options
        # ]),
        'imageUploadUrl': '/ckeditor5/upload/',
        'style': {
            'definitions': [
                {
                    'name': 'Custom Title',
                    'element': 'h2',
                    'classes': ['custom-title'],
                    'attributes': {'style': 'color: black;'}
                },
                {
                    'name': 'Callout Box',
                    'element': 'div',
                    'classes': ['callout-box'],
                    'attributes': {'style': 'border: 1px solid #ccc; padding: 10px;'}
                }
            ]
        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells'],
            'tableToolbar': ['insertTable', 'tableProperties', 'tableCellProperties'],
        },
        'tableProperties': {
            'defaultProperties': {
                'borderColor': '#000000',
                'borderWidth': '1px',
                'backgroundColor': '#ffffff',
            }
        }
    },
}