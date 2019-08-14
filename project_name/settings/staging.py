from .production import *

DEBUG = True

ALLOWED_HOSTS = ['fitzme-gateway.jx-staging.fitzme.xyz', 'localhost', '127.0.0.1']

MIDDLEWARE += ['app.middlewares.debug_middleware']
