# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import template
from django.template.loader import get_template

def welcome(request):
	a = 1
	return render_to_response("welcome.html",locals())
	return HttpResponse("hello")
