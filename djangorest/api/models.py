from django.db import models




class Gameslist(models.Model):
	title = models.CharField(max_length=225, blank=False, unique=True)
	console = models.CharField(max_length=50, blank=False, unique=True)
	releasedate = models.CharField(max_length=10, blank=False, unique=True)
	description = models.CharField(max_length=5000, blank=False, unique=True)
	fondmemories = models.CharField(max_length=10000, blank=False, unique=True)
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
