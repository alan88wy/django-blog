from pathlib import Path
import os
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Getting CLIENT_ID and CLIENT_SECRET from environment variable

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jn7gz@&@$68u246gp@v94+a1#bg@oy=@p*v0j!3@n*bbt6rw3v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cassandra_engine',
    'blog'
]

# INSTALLED_APPS = ['django_cassandra_engine'] + INSTALLED_APPS

SESSION_ENGINE = 'django_cassandra_engine.sessions.backends.db'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django_cassandra_engine',
        'NAME': 'awcrm',
        'OPTIONS': {
            'connection': {
                'auth_provider': PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET),
                'cloud': {
                    'secure_connect_bundle': '/Users/alan.wan/programming/astra/secure-connect-awcrm.zip'
                }
            }
        }
    }
}

# Local Cassandra

# DATABASES = {
#     'default': {
#         'ENGINE': 'django_cassandra_engine',
#         'NAME': 'mykeyspace',
#         'USER': 'user',
#         'PASSWORD': 'password',
#         'HOST': '127.0.0.1',  # comma separeted hosts
#         'OPTIONS': {
#             'replication': {
#                 'strategy_class': 'SimpleStrategy',
#                 'replication_factor': 3
#             },
#             'connection': {
#                 'consistency': ConsistencyLevel.LOCAL_QUORUM,
#                 'lazy_connect': True,
#                 'retry_connect': True,
#                 'port': 9042,
#                 'auth_provider': PlainTextAuthProvider(username=CLIENT_ID, password=CLIENT_SECRET),
#                 # + All connection options for cassandra.Cluster()
#             }
#         }
#     }
# }
#
# OR
# DATABASES = {
#     'default': {
#         'ENGINE': 'django_cassandra_engine',
#         'NAME': 'mykeyspace',
#         'USER': 'user',
#         'PASSWORD': 'password',
#         'HOST': '127.0.0.1',  # comma separeted hosts
#         'OPTIONS': {
#             'replication': {
#                 'strategy_class': 'SimpleStrategy',
#                 'replication_factor': 1
#             },
#             'connection': {
#                 'consistency': ConsistencyLevel.ONE,
#                 'lazy_connect': True,
#                 'retry_connect': True,
#                 'port': 9042,
#                 # + All connection options for cassandra.Cluster()
#             }
#         }
#     }
# }
#
# OR
# DATABASES = {
#     'default': {
#         'ENGINE': 'django_cassandra_engine',
#         'NAME': 'db',
#         'TEST_NAME': 'test_db',
#         'HOST': 'db1.example.com,db2.example.com',
#         'OPTIONS': {
#             'replication': {
#                 'strategy_class': 'SimpleStrategy',
#                 'replication_factor': 1
#             }
#         }
#     }
# }
#
# OR
# from cassandra import ConsistencyLevel

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     },
#     'cassandra': {
#         'ENGINE': 'django_cassandra_engine',
#         'NAME': 'db',
#         'USER': 'user',
#         'PASSWORD': 'pass',
#         'TEST_NAME': 'test_db',
#         'HOST': '127.0.0.1',
#         'OPTIONS': {
#             'replication': {
#                 'strategy_class': 'SimpleStrategy',
#                 'replication_factor': 1
#             },
#             'connection': {
#                 'consistency': ConsistencyLevel.LOCAL_ONE,
#                 'retry_connect': True
#                 # + All connection options for cassandra.cluster.Cluster()
#             },
#             'session': {
#                 'default_timeout': 10,
#                 'default_fetch_size': 10000
#                 # + All options for cassandra.cluster.Session()
#             }
#         }
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
