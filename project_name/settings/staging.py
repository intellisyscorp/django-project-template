from .production import *

DEBUG = True

ALLOWED_HOSTS = ['fitzme-gateway.jx-staging.fitzme.xyz', 'localhost']

MIDDLEWARE += ['app.middlewares.debug_middleware']
