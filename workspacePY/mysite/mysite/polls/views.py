# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def details(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def test(request):
    return HttpResponse("Test Success")