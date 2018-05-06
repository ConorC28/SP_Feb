import json
					#from django.views.generic.base import views
from django.shortcuts import render
from django.views.generic import TemplateView
					#from djangorest.forms import UploadGameForm
from django.shortcuts import render, redirect
from django.urls import path
from djangorest.forms import UploadGameForm
from djangorest.forms import UploadArticleForm

from django.db.models import Count
from django.db.models import Max

from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import StaticFilesStorage
from api.models import Articleslist
from api.models import ArticleslistForm
from api.models import Gameslist
from api.models import GameslistForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import update_session_auth_hash

import csv
from django.http import HttpResponse

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
		
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="multiTimeline.csv"'

	writer = csv.writer(response)
	writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
	writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

	return response	
	
	# Create the HttpResponse object with the appropriate CSV header.
    
	

def gamescolpage(request):
	#gameslistssimtitle = Gameslist.objects.filter(title__icontains='Overwatch')
	gamescount = Gameslist.objects.count()
	
	#ocount = Gameslist.objects.values('title').annotate(In_Collection=Count('title').aggregate(Max()))
	
	gameslists = Gameslist.objects.all()
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
	#gameslistssimtitle = Gameslist.objects.filter(title__icontains='Overwatch')
	gamescount = Gameslist.objects.count()
	
	bestgames = Gameslist.objects.values('title').order_by('-user_rating').distinct()
	
	ocount = Gameslist.objects.values('title').annotate(Counted=Count('title'))
	#titlecount = Gameslist.objects.values('title').count()
	#.order_by('-ocount')
	
	args = {'gamescount': gamescount, 'ocount' : ocount, 'bestgames' : bestgames}
	
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
			#Gameslist.game_pic = models.FileField(upload_to=user_directory_path)
			
			#Gameslist.game_pic = form.cleaned_data['game_pic']
			
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
			#Gameslist.game_pic = models.FileField(upload_to=user_directory_path)
			
			#Gameslist.game_pic = form.cleaned_data['game_pic']
			
			Gameslist.save()
			
		args = {'form': form}
		return render(request, self.template_name, args)