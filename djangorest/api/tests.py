from django.test import TestCase
from .models import Gameslist
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your tests here.

class ModelTestCase(TestCase):
	"""This class defones the test suite for the gameslist model"""

	def setup(self):
		self.gameslist_title = "zelda"
		self.gameslist_console = "N64"
		self.gameslist_score = "85"
		self.gameslist_description = "Amazing"
		self.gameslist_release_date = "2/2/98"
		self.gameslist_fond_memories = "Meow"
		self.gameslist  Gameslist(title=self,gameslist_title)
		self.gameslist  Gameslist(console=self,gameslist_console)
		self.gameslist  Gameslist(score=self,gameslist_score)
		self.gameslist  Gameslist(description=self,gameslist_description)
		self.gameslist  Gameslist(releasedate=self,gameslist_release_date)
		self.gameslist  Gameslist(fondmemories=self,gameslist_fond_memories)
	
	def test_model_can_create_a_gameslist(self):
		old_count = Gameslist.objects.count()
		self.gameslist.save()
		new_count = Gameslist.objects.count()
		self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):

	def url_test(self):
		"""Test url for home."""
		client = RequestsClient()
		response = client.get('home')
		assert response.status_code == 200


	def test_api_can_get_a_gameslist(self):
        """Test the api can get a given gameslist."""
        gameslist = Gameslist.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': Gameslist.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, gameslist)


#class ViewTestCase(TestCase):

	def setUp(self):
	
		self.client = APIClient()
		self.gameslist_data = {'title':'Zelda'}
		self.response = self.client.post(
			reverse('create'),
			self.gameslist_data,
			format="json")
	
	def test_api_can_create_a_gameslist(self):
		self.assertEqual(self.status_code, status.HTTP_201_CREATED)
	 
		
