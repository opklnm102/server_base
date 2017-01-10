from django.http import HttpResponse
from django.shortcuts import render


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
