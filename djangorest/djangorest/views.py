import json
#from django.views.generic.base import views
from django.shortcuts import render
from django.views.generic import TemplateView
#from djangorest.forms import UploadGameForm
from django.shortcuts import render
from django.urls import path
from djangorest.forms import UploadGameForm

from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import StaticFilesStorage

from api.models import Gameslist
from api.models import GameslistForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


# Create your views here.
def home(request):
	return render(
		request,
		'home.html',
		context = None)
		
def about(request):
	return render(
		request,
		'about.html',
		context = None)
		
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

#class addgames(TemplateView):
#	template_name = "addgames.html"

def addgames(request):
	
	gameslists = Gameslist.objects.all()
	
	args = {'gameslists': gameslists}
	
	return render(
		request, 
		'addgames.html',
		args)
		
	
	
		
		
		
	def submitform(request):
		if request.method == "POST":
			form = GameslistForm(request.POST)
			if form.is_valid():
			   form.save()
			   return render(request, 'newgameslist.html')
    
	
	#def get (self, request):
	#	form = UploadGameForm()
	#	return render(request, self.template_name, {'form': form})

def get (self,request):
	form = UploadGameForm()
	return render(request, '/templates/addgames.html', {'form': form})

		
