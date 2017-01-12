from django.conf.urls import (url, include)
from rest_framework import routers

from .views import PostViewSet

router = routers.DefaultRouter()
router.register(r'board', PostViewSet)

urlpatterns = [
    url(r'^post/', include(router.urls, namespace='post')),
]
