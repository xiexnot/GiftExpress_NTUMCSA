# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django import template
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.template import RequestContext

from lottery.models import Female, Male
# Create your views here.

def staff(request):
	current_female_number = len(Female.objects.all())
	current_male_number = len(Male.objects.all())
	noexchange_female_number = len(Female.objects.filter(exchange_flag = False))
	noexchange_male_number = len(Male.objects.filter(exchange_flag = False))

	if request.method == "POST" and  request.POST.has_key('set_male_number'):
		# set male number
		aim_male_number = int(request.POST['male_number'])
		Male.objects.all().delete()
		for i in range(aim_male_number):
			Male.objects.create(identify = (i+1) ,name = "男生"+str(i+1)+"號",exchange_flag = False,sex = "Male")

	if request.method == "POST" and  request.POST.has_key('set_female_number'):
		# set male number
		print request.POST
		aim_female_number = int(request.POST['female_number'])
		Female.objects.all().delete()
		for i in range(aim_female_number):
			Female.objects.create(identify = (i+1) ,name = "女生"+str(i+1)+"號",exchange_flag = False,sex = "Female")
	return render_to_response('staff.html',RequestContext(request,locals()))
