from django.http import HttpResponse
from django.shortcuts import render


def blog(request):
    return HttpResponse('olá')
