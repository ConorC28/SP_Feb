from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField          # Allows user multichoice for model, console - pip install django-multiselectfield
from django.forms import ModelForm

CONSOLE_CHOICES = (
				('Playstation', 'Playstation'), # The first element is what is added to the db and the second is what displays for the user selection
				('PC', 'PC'),
				('Commodore 64', 'Commodore 64'),
				('Nes', 'Nes'),
				('N64', 'N64'),
				('Snes/Famicom (multi region release)', 'Snes/Famicom (multi region release)'),
				('Snes(Europe release only)', 'Snes(Europe release only)'),
				('Famicom(North America release only)', 'Famicom(North America release only)'),
				('Famicom(Japan release only)', 'Famicom(Japan release only)'),
				('Gameboy', 'Gameboy'),
				('Gameboy Advanced', 'Gameboy Advanced'),
				('Nintendo DS', 'Nintendo DS'),
				('Nintendo 3DS', 'Nintendo 3DS'),
				('Nintendo Gamecube', 'Nintendo Gamecube'),
				('Nintendo Wii', 'Nintendo Wii'),
				('Nintendo WiiU', 'Nintendo WiiU'),
				('Nintendo Switch', 'Nintendo Switch'),
				('Sega Master System', 'Sega Master System'),
				('Sega Mega-Drive/Genesis', 'Sega Mega-Drive/Genesis'),
				('Sega Saturn', 'Sega Saturn'),
				('Sega Dreamcast', 'Sega Dreamcast'),
				('Sega Gamegear', 'Sega Gamegear'),
				('Sony Playstation','Sony Playstation'),
				('Sony Playstation 2','Sony Playstation 2'),
				('Sony Playstation 3','Sony Playstation 3'),
				('Sony Playstation 4','Sony Playstation 4'),
				('Microsoft Xbox', 'Microsoft Xbox'),
				('Microsoft Xbox360', 'Microsoft Xbox360'),
				('Microsoft XboxONE', 'Microsoft XboxONE'))
				
RATING_CHOICES = (('0.5', '0.5'), # The first element is what is added to the db and the second is what displays for the user selection
				('1.0', '1.0'),
				('1.5', '1.5'),
				('2.0', '2.0'),
				('2.5', '2.5'),
				('3.0', '3.0'),
				('3.5', '3.5'),
				('4.0', '4.0'),
				('4.5', '4.5'),
				('5.0', '5.0'),
				('5.5', '5.5'),
				('6.0', '6.0'),
				('6.5', '6.5'),
				('7.0', '7.0'),
				('7.5', '7.5'),
				('8.0', '8.0'),
				('8.5', '8.5'),
				('9.0', '9.0'),
				('9.5', '9.5'),
				('10', '10'))
				

#COLLECTOR_STATUS_CHOICES = (('item_key1', 'Keeping'),
#			('item_key2', 'Trading'),
#			('item_key3', 'Selling'))
		
class Gameslist(models.Model):
	title = models.CharField(max_length=225, blank=False, unique=False)
	console = MultiSelectField(choices=CONSOLE_CHOICES)
	user_rating = MultiSelectField(choices=RATING_CHOICES)
	#collector_status = MultiSelectField(choices=COLLECTOR_STATUS_CHOICES)
	#release_date = models.DateField(default=datetime.now, blank=True)
	release_date = models.DateField(blank=True, null=True)
	description = models.CharField(max_length=5000, blank=False, unique=False)
	fond_memories = models.CharField(max_length=10000, blank=False, unique=False)
	game_pic = models.ImageField(upload_to = 'game_image', default = 'game_image')
	owner = models.ForeignKey('auth.User',
	related_name='gameslists',
	on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	
class GameslistForm(ModelForm):
	class Meta:
		model = Gameslist()
		fields = "__all__"
	
	
	def __str__(self):
		"""Return a human readable version"""
		return "{}".format(self.name)
	

# Create your models here.
