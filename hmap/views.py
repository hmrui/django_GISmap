from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index_action(request):
    return render(request, 'hmap/index.html', {})

def DataCity_action(request):
    return render(request, 'hmap/DataCity.html', {})

