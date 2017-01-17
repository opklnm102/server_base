from django.conf.urls import (url, include)
from rest_framework import routers

from .views import PostViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    url(r'^', include(router.urls, namespace='post')),
]
