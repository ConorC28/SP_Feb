import json
#from django.views.generic.base import views
from django.shortcuts import render
from django.views.generic import TemplateView
#from djangorest.forms import UploadGameForm
from django.shortcuts import render
from django.urls import path

# Create your views here.
def home(request):
	return render(
		request,
		'about.html',
		context = None)
		
def about(request):
	return render(
		request,
		'about.html',
		context = None)

#class addgames(TemplateView):
#	template_name = "addgames.html"

def addgames(request):
	return render(
		request,
		'addgames.html',
		context = None)
	
	#def get (self, request):
	#	form = UploadGameForm()
	#	return render(request, self.template_name, {'form': form})

def news(request):
	return render(
		request,
		'news.html',
		context = None)
		
def trends(request):
	return render(
		request,
		'trends.html',
		context = None)
		
