"""danbi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from danbi import views

urlpatterns = [
    # django
    url(r'^health.txt$', views.health_check,
        name='health_check'),
    url(r'^admin/', admin.site.urls),
    # 3rd party
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # local
    url(r'^$', views.home, name='home'),
    url(r'^404/$', views.handler404, name='error404'),
    url(r'^500/$', views.handler500, name='error500'),
    url(r'^500/sentry/$', views.raise_sentry_error, name='error500-sentry'),

    url(r'^sample/', include('sample.urls', namespace='sample')),
    url(r'^board/', include('board.urls', namespace='board')),
    url(r'^summernote/', include('django_summernote.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
