try:
    from .settings import *
except ImportError:
    pass
import requests


DEBUG = True

ALLOWED_HOSTS.append(".ap-northeast-1.elb.amazonaws.com")
EC2_PRIVATE_IP = None
try:
    EC2_PRIVATE_IP = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', timeout=0.02).text
except requests.exceptions.RequestException:
    pass

if EC2_PRIVATE_IP:
    ALLOWED_HOSTS.append(EC2_PRIVATE_IP)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'dev-danbi.cuqc4ixq3fe2.ap-northeast-1.rds.amazonaws.com',
        'NAME': 'staging_danbi_server_base',
        'USER': 'danbi_server_base',
        'PASSWORD': 'QeW64XurIak',
    },
    'slave': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'dev-danbi-slave.cuqc4ixq3fe2.ap-northeast-1.rds.amazonaws.com',
        'NAME': 'staging_danbi_server_base',
        'USER': 'danbi_server_base',
        'PASSWORD': 'QeW64XurIak',
    },
    'standalone': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'dev-danbi.cuqc4ixq3fe2.ap-northeast-1.rds.amazonaws.com',
        'NAME': 'staging_danbi_server_base',
        'USER': 'danbi_server_base',
        'PASSWORD': 'QeW64XurIak',
    }
}

# REST FRAMEWORK
REST_FRAMEWORK.update({'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',)})

# SENTRY
RAVEN_CONFIG = {
    'dsn': 'https://5c9defa873e8464faa10488658c78714:a41e218d23b14bbca41514a2cde70a79@sentry.io/139503',
}

# CELERY
CELERY_BROKER_URL = 'redis://server-base-broker.kqnzd3.0001.apne1.cache.amazonaws.com:6379/0'
