from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField          # Allows user multichoice for model, console - pip install django-multiselectfield

CONSOLE_CHOICES = (('Playststion', 'Playstation'), # The first element is what is added to the db and the second is what displays for the user selection
				('Nes', 'Nes'),
				('N64', 'N64'),
				('Snes/Famicom (multi region release)', 'Snes/Famicom (multi region release)'),
				('Snes(Europe release only)', 'Snes(Europe release only)'),
				('Famicom(North America release only)', 'Famicom(North America release only)'),
				('Famicom(Japan release only)', 'Famicom(Japan release only)'),
				('Gameboy', 'Gameboy'),
				('Gameboy Advanced', 'Gameboy Advanced'),
				('Sega mega-drive', 'Sega mega-drive'))

#COLLECTOR_STATUS_CHOICES = (('item_key1', 'Keeping'),
#			('item_key2', 'Trading'),
#			('item_key3', 'Selling'))
		
class Gameslist(models.Model):
	title = models.CharField(max_length=225, blank=False, unique=False)
	console = MultiSelectField(choices=CONSOLE_CHOICES)
	#collector_status = MultiSelectField(choices=COLLECTOR_STATUS_CHOICES)
	release_date = models.CharField(max_length=10, blank=False, unique=False)
	description = models.CharField(max_length=5000, blank=False, unique=False)
	fond_memories = models.CharField(max_length=10000, blank=False, unique=False)
	game_pic = models.ImageField(upload_to = 'staticfiles/', default = 'staticfiles/None/no-img.jpg')
	owner = models.ForeignKey('auth.User',
	related_name='gameslists',
	on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	
	
	
	
	def __str__(self):
		"""Return a human readable version"""
		return "{}".format(self.name)
	

# Create your models here.
