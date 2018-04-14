import json
					#from django.views.generic.base import views
from django.shortcuts import render
from django.views.generic import TemplateView
					#from djangorest.forms import UploadGameForm
from django.shortcuts import render, redirect
from django.urls import path
from djangorest.forms import UploadGameForm

from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import StaticFilesStorage

from api.models import Gameslist
from api.models import GameslistForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.models import User 
					#from django.contrib.auth.forms import RegistrationForm
from djangorest.forms import ( 
	RegistrationForm,
	EditProfileForm	
	)
	
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
					# Imports for csv file
#import csv
#from django.http import HttpResponse



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
	
	gameslists = Gameslist.objects.all()
	# Filter below displays only a users gameslist when on the profile page
	args = {'user': request.user, 'gameslists': gameslists.filter(owner=request.user)}
	return render(
		request,
		'profile.html',
		args)

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
	
		
def welcome(request):
	return render(
		request,
		'welcome.html',
		context = None)
		

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/home')
	else:
		form = RegistrationForm()
		
		args = {'form': form}
	return render(request, 'register.html', args)

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

class AddGames(TemplateView):
	template_name = 'addgames.html'
	queryset = Gameslist.objects.all()
	
	def get(self, request):
		form = UploadGameForm()
		return render(request, self.template_name, {'form': form})
		
	def post(self, request):
		form = UploadGameForm(request.POST)
		if form.is_valid():
			Gameslist = form.save()
			Gameslist.user = request.user
			Gameslist.save()
			
		args = {'form': form}
		return render(request, self.template_name, args)
#def addgames(request):
#	return render(
#		request,
#		'addgames.html',
#		context = None)
		
	#if request.method == "POST":
	#	form = UserCreationForm(request.POST)
	#	if form.is_valid():
	#		form.save()
	#	return redirect('/home')
	#else:
	#	form = UserCreationForm()
	#	
	#	args = {'form': form}
	#return render(request, 'register.html', args)	
		
	
		
		
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

def gamescolpage(request):
	
	gameslists = Gameslist.objects.all()
	
	args = {'gameslists': gameslists}
	
	return render(
		request, 
		'gamescolpage.html',
		args)
		
	
	
		
		
		
#	def submitform(request):
#		if request.method == "POST":
#			form = GameslistForm(request.POST)
#			if form.is_valid():
#			   form.save()
#			   return render(request, 'newgameslist.html')
    
	
	#def get (self, request):
	#	form = UploadGameForm()
	#	return render(request, self.template_name, {'form': form})

#def get (self,request):
#	form = UploadGameForm()
#	return render(request, '/templates/addgames.html', {'form': form})

		
