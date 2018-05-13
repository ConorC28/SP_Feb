from django import forms
from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
#from api.models import UserProfile
from multiselectfield import MultiSelectField          # Allows user multichoice for model, console - pip install django-multiselectfield
from django.forms import ModelForm
from api.models import Gameslist
from api.models import Articleslist

from django.contrib.auth.forms import UserCreationForm, UserChangeForm # Import to allow custom user creation form

from django.core.files.images import get_image_dimensions

class UploadGameForm(forms.ModelForm):

	class Meta:
		model = Gameslist
		
		fields = ('title','console', 'score', 'release_date','description','fond_memories','game_pic',)
		#model.fond_memories = forms.CharField(widget=forms.Textarea)
		#title = models.CharField(max_length=100)
		#game_pic = models.FileField(upload_to = 'game_image', default = 'game_image')


#class EditGameForm(forms.ModelForm):
	
#	class Meta:
#		model = Gameslist
#		
#		fields = ('title','console', 'score', 'release_date','description','fond_memories','game_pic',)

								# Form to editprofile
class EditProfileForm(UserChangeForm):
	
	class Meta:
		model = User
		fields =  (
			'username',
			'first_name',
			'last_name',
			'email',
			'password'
			
		)
	
		
								# Form to create user
class RegistrationForm(UserCreationForm):
	
	
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1'
			
		)
	
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		
		
		if commit:
			user.save()
			
		return user
								# Form to allow upload to gamelist from front end

class UploadArticleForm(forms.ModelForm):

	class Meta:
		model = Articleslist
		
		fields = ('title','content1','content2','content3','content4')
	
	
	