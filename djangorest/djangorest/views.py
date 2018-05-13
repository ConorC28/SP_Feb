import json
					#from django.views.generic.base import views
from django.shortcuts import render
from django.views.generic import TemplateView
					#from djangorest.forms import UploadGameForm
from django.shortcuts import render, redirect
from django.urls import path
from djangorest.forms import UploadGameForm
#from djangorest.forms import EditGameForm
from djangorest.forms import UploadArticleForm
from django.conf.urls import url
from django.contrib.auth.models import User
from django.db.models.functions import Lower
from django.db.models import Count
from django.db.models import Min
from django.db.models import Max

from django.core.signals import request_finished

from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import StaticFilesStorage
from api.models import Articleslist
from api.models import ArticleslistForm
from api.models import Gameslist
from api.models import GameslistForm
from api.models import Newslist
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import update_session_auth_hash

from django.views.generic.edit import DeleteView

import csv
from django.http import HttpRequest

# Imports for Pusher chat

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import csv

# Import to allow multiple filter query

from django.db.models import Q


from django.contrib.auth.models import User 
					#from django.contrib.auth.forms import RegistrationForm
from djangorest.forms import ( 
	RegistrationForm,
	EditProfileForm	
	)
	
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
					
# Imports for pusher

#render library for returning views to the browser
from django.shortcuts import render
#decorator to make a function only accessible to registered users
from django.contrib.auth.decorators import login_required
#import the user library
from pusher import Pusher
#replace the xxx with your app_id, key and secret respectively
#instantate the pusher class
pusher = Pusher(app_id=u'509489', key=u'1f1bc9d8a82330c22c7d', secret=u'09c8901c9ed76b834847', cluster=u'eu')
# Create your views here.
#login required to access this page. will redirect to admin login page.
@login_required(login_url='log/') 



def chat(request):
    return render(request,"chat.html");

@csrf_exempt
def broadcast(request):
    pusher.trigger(u'a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
    return HttpResponse("done");

def changepassword(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('profile')
		else:
			return render(request, 'changepassword.html', {'badcred': True})

	else:
		form = PasswordChangeForm(user=request.user)
		
		args = {'form': form}
		return render(request, 'changepassword.html', args)

def login(request):
	if form.is_valid():
		return redirect('profile')
	
	return render(
		request,
		'login.html',
		context = None)

def usergames(request):
	
	return render(
		request,
		'usergames.html',
		context = None)
			
def profile(request):
	# Getting all objects
	gameslists = Gameslist.objects.all()
	
	args = {'user': request.user, # filter to only display the users uploads
			'gameslists': gameslists.filter(owner=request.user),
			 
			}
	return render(
		request,
		'profile.html',
		args)
		
	# Takes Id as argument, this is set in profile in the url link
def deletegame(request, id):
	gameslists = Gameslist.objects.all()
	
	# setting the id, the deleting the game
	Gameslist.objects.get(id=id)
	gameslist = get_object_or_404(Gameslist, id=id).delete()
	args = { 
			'gameslists': gameslists.filter(owner=request.user),
			}
	return render(request, 'profile.html', args)
	
	# Takes Id as argument, this is set in profilee in the url link
def editgame(request, id):
	
	gameslist = get_object_or_404(Gameslist, id=id)
	
	gameslists = Gameslist.objects.all()
	Gameslist.objects.get(id=id)
	    
	args = { 'gameslist':gameslist,
			'gameslists': gameslists,
			}
		
	# Passing in the current instance of gameslist attributed to the id
	if request.method == 'POST':
		form = UploadGameForm(request.POST, instance=gameslist) 
		
		if form.is_valid():
						
			
			form.save()
			return redirect('profile')
			
	else:
		form = UploadGameForm(instance=gameslist)
		
		args = {'form': form}
		return render(request, 'editgame.html', args)		

			

def edit(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		
		if form.is_valid():
			form.save()
			return redirect('profile')
			
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form}
		return render(request, 'edit.html', args)
	
		
def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/login')
		else:
			return render(request, 'register.html', {'badlogcred': True})
	else:
		form = RegistrationForm()
		
		args = {'form': form}
	return render(request, 'register.html', args)
	
def home(request):
	return render(
		request,
		'home.html',
		context = None)
		
def welcome(request):
	return render(
		request,
		'welcome.html',
		context = None)

	# Takes pk as argument, this is set in gamescolpage in the url link
def oug(request, pk):
	
	Gameslist.objects.get(pk=pk)
	gameslists = Gameslist.objects.all()
		
	gameslist = get_object_or_404(Gameslist, pk=pk)
	
	args = { 'gameslist':gameslist,
			'gameslists': gameslists.filter(owner=request.user),
						
			}
	return render(
		request,
		'otherusersgames.html',		
		args
		)
		 
		
def about(request):
	return render(
		request,
		'about.html',
		context = None)
		
def news(request):
	newslists = Newslist.objects.all()
	
	args = {'newslists': newslists}

	return render(
		request,
		'news.html',
		args)
		
def trends(request):
	
	
	return render(
		request,
		'trends.html',
		context = None)	
	
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="multiTimeline.csv"'

	writer = csv.writer(response)
	writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
	writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

	return response
		

def gamescol(request):	
	
	gameslists = Gameslist.objects.all()
	# Getting q from gamescolpage & filtering the query
	query = request.GET.get("q")
	if query:
		gameslists = gameslists.filter(
			Q(title__icontains=query) |
			Q(console__icontains=query) |
			Q(owner__username__icontains=query)
			).distinct()
		
	args = {'gameslists': gameslists}
	
	return render(
		request, 
		'gamescolpage.html',
		args)
		
def gamesdata(request):	
	# setting varies sets of the Gameslist to display
	gamescount = Gameslist.objects.count()
	gameslists = Gameslist.objects.all()
	bestgames = Gameslist.objects.values('title','score','owner',).order_by('-score').distinct()
	worstgames = Gameslist.objects.values('title','score','owner',).order_by('score').distinct()
	collectedcount = Gameslist.objects.annotate(lower_title=Lower('title')).values('lower_title').annotate(num=Count('lower_title')).order_by('-num')
	owner = Gameslist.owner
	
	
	# Setting these arguments	
	args = {
		'worstgames':worstgames,
		'owner':owner,
		'gameslists': gameslists,
		'gamescount': gamescount,
		'collectedcount' : collectedcount,
		'bestgames' : bestgames}
	# Passing in the arguments
	return render(
		request, 
		'gamesdata.html',
		args)
	
def userarticles(request):
	
	articleslists = Articleslist.objects.all()
	
	args = {'articleslists': articleslists}
	
	return render(
		request, 
		'userarticles.html',
		args)
	
	# class views used here to render templates to pass model fields into template 
class AddArticles(TemplateView):
	template_name = 'addarticles.html'
	queryset = Articleslist.objects.all()

	def get(self, request):
		form = UploadArticleForm()
		
		return render(request, self.template_name, {'form': form})
		
		#Request files here and additions in the html file allow for image upload from front
	def post(self, request):
		form = UploadArticleForm(request.POST, request.FILES)
		if form.is_valid():
			Articleslist = form.save(commit=False)
			Articleslist.owner = request.user
						
			Articleslist.save()
			
		args = {'form': form}
		return render(request, self.template_name, args)

class AddGames(TemplateView):
	template_name = 'addgames.html'
	queryset = Gameslist.objects.all()
	
	def get(self, request):
		form = UploadGameForm()
		
		return render(request, self.template_name, {'form': form})
		#Request files here and additions in the html file allow for image upload from front
	def post(self, request):
		form = UploadGameForm(request.POST, request.FILES)
		if form.is_valid():
			Gameslist = form.save(commit=False)
			Gameslist.owner = request.user
						
			Gameslist.save()
			
		args = {'form': form,
		'queryset': queryset.filter(owner=request.user),}
		return render(request, 'profile.html', args)
		
