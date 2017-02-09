try:
    from .settings import *
except ImportError:
    pass

INTERNAL_IPS = ['127.0.0.1']
INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
