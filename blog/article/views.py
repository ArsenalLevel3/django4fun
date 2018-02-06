# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse("hello world, Django!")

def detail(request, my_args):
    return HttpResponse("You're looking at my_args % s." % my_args)
    

