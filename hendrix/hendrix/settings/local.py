from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hendrix',
        'USER': 'hendrix',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
