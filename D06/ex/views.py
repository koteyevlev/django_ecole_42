import datetime
from random import choice

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.

def session(request):
    response = render(request, 'user.html')
    if not request.COOKIES.get('user'):
        random_user = choice(settings.RANDOM_USERS)
        request.COOKIES['user'] = random_user
        response = render(request, 'user.html')
        response.set_cookie('user', random_user, max_age=42)
    return response


def sign_in(request):
    return HttpResponse("Not implemented")


def sign_up(request):
    return HttpResponse("Not implemented")
