from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Gameslist
from .models import Articleslist
from .models import Newslist
from rest_framework.validators import UniqueValidator


#class UserSerializer(serializers.ModelSerializer):
#	email = serializers.EmailField(
#			required=True,
#			validators=[UniqueValidator(queryset=User.objects.all())]
#			)
#	username = serializers.CharField(
#			validators=[UniqueValidator(queryset=User.objects.all())]
#			)
#	password = serializers.CharField(min_length=8)
#	
#	def create(self, validated_data):
#		user = User.objects.create_user(validated_data['username'], validated_data['email'],
#			validated_data['password'])
#		
#		return user
#	
#	class Meta:
#		model = Userfields = ('id', 'username', 'email', 'password')

class GameslistSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		"""Meta class to map serializers fields with the model fields"""
		model = Gameslist
		fields = ('id', 'title', 'console', 'user_rating', 'release_date', 'description', 'fond_memories', 'game_pic', 'owner', 'date_created','date_modified')
		read_only_fields = ('date_modified', 'date_crereated')

class ArticleslistSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		"""Meta class to map serializers fields with the model fields"""
		model = Articleslist
		fields = ('id', 'title', 'content', 'owner', 'date_created','date_modified')
		read_only_fields = ('date_modified', 'date_crereated')
		
class NewslistSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		"""Meta class to map serializers fields with the model fields"""
		model = Newslist
		fields = ('id', 'title', 'content', 'owner', 'date_created','date_modified')
		read_only_fields = ('date_modified', 'date_crereated')