try:
    from .settings import *
except ImportError:
    pass

DEBUG = True

# REST FRAMEWORK
REST_FRAMEWORK.update({'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',)})
