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
    'admin_honeypot',
    'django_ckeditor_5',
    # my apps
    'category',
    'blog',
    'user',
    'store',
    'stack',
    'purchase',
    'dashboard',
    'messaging',
    # 'gateways'
]

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


# CKEditor configs:
# CKEDITOR_UPLOAD_PATH = MEDIA_ROOT / 'posts/'
# CKEDITOR_IMAGE_BACKEND = f'{MEDIA_URL}posts'
# CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
# CKEDITOR_CONFIGS = {
#     'default':
#         {
#             'toolbar': 'full',
#             'width': 'auto',
#             'extraPlugins': ','.join([
#                 'codesnippet',
#             ]),
#         },
# }

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|', 'bold', 'italic', 'underline', 'strikethrough', 'link',
            'alignment', 'fontSize', 'fontColor', 'fontBackgroundColor', 'highlight',
            'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', 'insertTable', 
            'mediaEmbed', '|', 'undo', 'redo'
        ],
        'height': 400,
        'width': '100%',
        'fontColor': {
            'columns': 5,
            'colors': [
                { 'color': 'hsl(0, 75%, 60%)', 'label': 'Red' },
                { 'color': 'hsl(30, 75%, 60%)', 'label': 'Orange' },
                # ... more colors
            ]
        },
        'fontSize': {
            'options': [9, 11, 13, 'default', 17, 19, 21],
            'supportAllValues': True
        },
        'highlight': {
            'options': [
                { 'model': 'yellowMarker', 'class': 'marker-yellow', 'title': 'Yellow Marker', 'color': 'var(--ck-highlight-marker-yellow)' },
                # ... other highlights
            ]
        },
        'mediaEmbed': {
            'previewsInData': True,
            'providers': [
                'youtube', 'vimeo', 'dailymotion', 'twitch', 'facebook', 'instagram'
            ]
        },
        # 'extraPlugins': ','.join([
        #     'uploadimage',  # Image upload support
        #     'font',         # Font styling options
        #     'alignment',    # Text alignment options
        #     'highlight',    # Text highlighting options
        # ]),
        'imageUploadUrl': '/ckeditor5/upload/',  # Make sure this URL is set correctly
        
        'style': {
            'definitions': [
                {
                    'name': 'Custom Title',
                    'element': 'h2',
                    'classes': ['custom-title'],
                    'attributes': {'style': 'color: blue;'}
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