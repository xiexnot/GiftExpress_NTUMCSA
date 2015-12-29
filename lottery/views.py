# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django import template
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.template import RequestContext
# Create your views here.

from lottery.models import Female, Male

import os
import sys
import time
import json
import random

def isLastPerson():
	count_A = len(Female.objects.filter(exchange_flag = False))
	count_B = len(Male.objects.filter(exchange_flag = False))
	if count_A + count_B == 1:
		return True
	return False

def theLastPerson():
	try:
		tmp = Male.objects.filter(exchange_flag = False)[0].name
		Male.objects.filter(exchange_flag = False).update(exchange_flag = True)
	except:
		pass
	try:
		tmp = Female.objects.filter(exchange_flag = False)[0].name
		Female.objects.filter(exchange_flag = False).update(exchange_flag = True)
	except:
		pass
	return tmp

def SelectMale():
	Lists = Male.objects.filter(exchange_flag = False)
	if len(Lists)==0:
		return False, []
	select = Lists[random.randint(0,len(Lists)-1)].identify
	Male.objects.filter(identify = select).update(exchange_flag = True)
	ans = Male.objects.filter(identify = select)[0].name
	return True, ans

def SelectFemale():
	Lists = Female.objects.filter(exchange_flag = False)
	if len(Lists)==0:
		return False, []
	select = Lists[random.randint(0,len(Lists)-1)].identify
	Female.objects.filter(identify = select).update(exchange_flag = True)
	ans = Female.objects.filter(identify = select)[0].name
	return True, ans

def lottery(request):
#	if request.method == "GET":
#		return render_to_response('welcome.html',locals())
	current_female_number = len(Female.objects.all())
	current_male_number = len(Male.objects.all())
	noexchange_female_number = len(Female.objects.filter(exchange_flag = False))
	noexchange_male_number = len(Male.objects.filter(exchange_flag = False))

	if request.method == "POST":
		if request.POST.has_key("tryit"):
			matchA = []
			matchB = []
			matchTmp = ""
			while len(matchA)<5 and len(matchB)<5 :

				flag_A, A = SelectMale()
				flag_B, B = SelectFemale()

				if flag_A == False:
					flag_A, A = SelectFemale()

				if flag_B == False:
					flag_B, B = SelectMale()

				matchA.append(A)
				matchB.append(B)
				print A,' ',B
				if isLastPerson():
					matchTmp = theLastPerson()
					break
				pass

			current_time = time.time()
			return render_to_response('lottery.html',RequestContext(request,locals()))
	return render_to_response('lottery.html',RequestContext(request,locals()))
