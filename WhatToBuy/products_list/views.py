from django.shortcuts import render
from django.http import HttpResponse

def hello(request, anything):
    return HttpResponse(f'Potato Wars {anything}?')

def hello2(request):
    anything = request.GET.get("situation")
    return HttpResponse(f'Potato Wars {anything}?')