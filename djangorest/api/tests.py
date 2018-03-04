from django.test import TestCase
from .models import Gameslist
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your tests here.

class ViewTestCase(TestCase):

	def setUp(self):
	
		self.client = APIClient()
		self.gameslist_data = {'title':'Zelds'}
		self.response = self.client.post(
			reverse('create'),
			self.gameslist_data,
			format="json")
	
	def test_api_can_create_a_gameslist(self):
		self.assertEqual(self.status_code, status.HTTP_201_CREATED)

#class ModelTestCase(TestCase):
#	"""This class defones the test suite for the gameslist model"""
	
#	def setup(self):
#		self.gameslist_title = "zelda"
#		self.gameslist_console = "N64"
#		self.gameslist_description = "Amazing"
#		self.gameslist_releasedate = "98"
#		self.gameslist_fondmemories = "Meow"
#		self.gameslist  Gameslist(title=self,gameslist_title)
#		self.gameslist  Gameslist(console=self,gameslist_console)
	#	self.gameslist  Gameslist(description=self,gameslist_description)
	#	self.gameslist  Gameslist(releasedate=self,gameslist_releasedate)
#		self.gameslist  Gameslist(fondmemories=self,gameslist_fondmemories)
#	
#	def test_model_can_create_a_gameslist(self):
#		old_count = Gameslist.objects.count()
#		self.gameslist.save()
#		new_count = Gameslist.objects.count()
#		self.assertNotEqual(old_count, new_count)