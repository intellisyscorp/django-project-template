from .base import *

DEBUG = False

ALLOWED_HOSTS = ['fitzme-gateway.jx-production.fitzme.co.kr', 'localhost', '127.0.0.1']

LOGGING['loggers']['']['level'] = 'INFO'

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
    # 'rest_framework.renderers.BrowsableAPIRenderer',
)
