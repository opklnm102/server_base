"""
WSGI config for danbi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# development, testing, staging, production
DEPLOYMENT_LEVEL = os.environ.setdefault("DEPLOYMENT_LEVEL", "development")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"danbi.settings_{DEPLOYMENT_LEVEL}")

application = get_wsgi_application()
