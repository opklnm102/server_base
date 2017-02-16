from django.http import HttpResponse
from django.shortcuts import render
from raven.contrib.django.raven_compat.models import client


def home(request):
    return render(request, 'home.html', {'test': True})


def health_check(request):
    return HttpResponse('OK', content_type='text/plain')


def handler404(request):
    response = render(request, "404.html")
    response.status_code = 404
    return response


def handler500(request):
    response = render(request, "500.html")
    response.status_code = 500
    return response


class SentryTestException(Exception):
    pass


def raise_sentry_error(request):
    response = render(request, "500.html")
    response.status_code = 500
    try:
        raise SentryTestException
    except SentryTestException:
        client.captureException()
    return response
