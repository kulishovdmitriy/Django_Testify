import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB_TEST'),
        'USER': os.environ.get('POSTGRES_USER_TEST'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD_TEST'),
        'HOST': os.environ.get('POSTGRES_HOST_TEST'),
        'PORT': os.environ.get('POSTGRES_PORT_TEST'),
    }
}
