
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.template import resolve_variable

#register = Library()

from django.shortcuts import render
from django.template import *
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth 
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string

#from forms import Registration
from users.models import Detail
from users.forms import Choice

import sys
sys.path.insert(0,'parser/directory')
from parser import *


#from django.views.generic.base import TemplateView
#from django.views.generic import TemplateView

# Create your views here.


"""
def userview(request):
	user = "PSC"
	html = "<html><body>This is %s </body></html>" %user
	return RenderResponse(html)


def test(request):
	test = "PaHuuuuuuu"
	html = "<html><body>Test Username is %s </body></html>" % test
	return HttpResponse(html)
"""

def test2(request):
	#test = "Test View"
	#args = request.GET.get("city")
	#print request.GET.get('city', '')

	return HttpResponse("Hello")	

def login(request):
	c = {}
	#args = {}
	c.update(csrf(request))
	return render_to_response("login.html", c)

def test(request):
	test = "PaHuuuuuuu"
	html = "<html><body>Test Username is %s </body></html>" % test
	return HttpResponse(html)

def homepage(request, city=""):
	data = Detail.objects.all()

	p = Detail.objects.get(id=1)

	print p
	
	url = "http://127.0.0.1:8000/Bangalore"
	#print data 
	#print request.GET

	#category = Choice.objects.all()
	#cname = request.POST.get('city')

	#city = request.POST['city']
	#print city

	myString = "THis is a python string"

	form = Choice()

	city = request.path

	city = city.strip("/")

	#if form.is_valid():
		#answer = form.cleaned_data['value']
        
        #print answer

	return TemplateResponse(request, 'homepage.html', {"data": data, "form": form, "city": city} )


def city(request):
	#args = request.GET()
	#req = resolve_variable('request', context)
		#print req
	#args = request.GET.('city', '')
    
    #if request.method == "POST":
    	#form = Reg
    #	print(request.POST)
    #r = request.GET.post('city', '')
	data = Detail.objects.all()

	print data 
	print request.GET

	myString = "THis is a python string"
	return TemplateResponse(request, 'city.html', {"data": data})
	#return HttpResponse(request.POST.get('city', ''))
	
