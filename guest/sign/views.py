# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, "index.html")


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            return HttpResponseRedirect('event_manage/')
        else:
            return render(request, 'index.html', {'error': 'username or password error!!'})
    else:
        return render(request, 'index.html', {'error':'username or password error!!'})


def event_manage(request):
    return render(request, "event_manage.html")
    