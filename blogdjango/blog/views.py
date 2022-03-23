from http.client import HTTPResponse
from django.shortcuts import render


def blog(request):
    render(HTTPResponse('olá'))
