from django import forms
from multiselectfield import MultiSelectField



class UploadGameForm(forms.Form):
	
	CONSOLE_CHOICES = (('Playststion', 'Playstation'), # The first element is what is added to the db and the second is what displays for the user selection
					('Commodore 64', 'Commodore 64'),
					('Nes', 'Nes'),
					('N64', 'N64'),
					('Snes/Famicom (multi region release)', 'Snes/Famicom (multi region release)'),
					('Snes(Europe release only)', 'Snes(Europe release only)'),
					('Famicom(North America release only)', 'Famicom(North America release only)'),
					('Famicom(Japan release only)', 'Famicom(Japan release only)'),
					('Gameboy', 'Gameboy'),
					('Gameboy Advanced', 'Gameboy Advanced'),
					('Nintendo Gamecube', 'Nintendo Gamecube'),
					('Sega Master System', 'Sega Master System'),
					('Sega Mega-Drive/Genesis', 'Sega Mega-Drive/Genesis'),
					('Sega Saturn', 'Sega Saturn'),
					('Sega Dreamcast', 'Sega Dreamcast'),
					('Sega Gamegear', 'Sega Gamegear'),
					('Sony Playstation','Sony Playstation'),
					('Sony Playstation 2','Sony Playstation 2'),
					('Microsoft Xbox', 'Microsoft Xbox'))
				
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


	title = forms.CharField()
	console = MultiSelectField(choices=CONSOLE_CHOICES)
	user_rating = MultiSelectField(choices=RATING_CHOICES)
	#collector_status = MultiSelectField(choices=COLLECTOR_STATUS_CHOICES)
	#release_date = models.DateField(default=datetime.now, blank=True)
	release_date = forms.CharField()
	description = forms.CharField()
	fond_memories = forms.CharField()
	#game_pic = forms.ImageField(upload_to = 'staticfiles/', default = 'staticfiles/None/no-img.jpg')
	#owner = forms.ForeignKey('auth.User',
	#related_name='gameslists',
	#on_delete=forms.CASCADE)
	#date_created = forms.DateTimeField(auto_now_add=True)
	#date_modified = forms.DateTimeField(auto_now=True)