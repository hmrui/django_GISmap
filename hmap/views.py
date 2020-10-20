from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index_action(request):
    return render(request, 'hmap/1.html', {})


def screw_action(request):
    return HttpResponse("陈一飞是个大傻b")
