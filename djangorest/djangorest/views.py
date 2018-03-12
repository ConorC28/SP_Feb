import json
#from django.views.generic.base import views
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home(request):
	return render(
		request,
		'index.html',
		context = None)
		
def about(request):
	return render(
		request,
		'about.html',
		context = None)