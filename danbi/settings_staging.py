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

# REST FRAMEWORK
REST_FRAMEWORK.update({'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',)})
