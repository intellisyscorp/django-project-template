from .base import *

# use temp psql for devpod must create and drop! manually
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': f'{os.environ["HOSTNAME"]}-{{ project_name }}',
        'USER': 'test',
        'PASSWORD': 'test',
        'HOST': 'dev-db.jx-develop',
        'PORT': ''
    }
}