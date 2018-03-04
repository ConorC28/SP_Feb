from rest_framework import serializers
from .models import Gameslist

class GameslistSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		"""Meta class to map serializers fields with the model fields"""
		model = Gameslist
		fields = ('id', 'title', 'console', 'releasedate', 'description', 'fondmemories', 'game_pic', 'owner', 'date_created','date_modified')
		read_only_fields = ('date_modified', 'date_crereated')

