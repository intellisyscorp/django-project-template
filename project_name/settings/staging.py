from .production import *

DEBUG = True

ALLOWED_HOSTS = ['fitzme-gateway.jx-staging.fitzme.xyz', 'localhost', '127.0.0.1']

LOGGING['loggers']['']['level'] = 'DEBUG'

MIDDLEWARE += ['app.middlewares.debug_middleware']

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
)
