from rest_framework import generics
from .serializers import GameslistSerializer
from .models import Gameslist
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import serializers
#from api.serializers import UserSerializer
from rest_framework import status
from .permissions import IsOwnerOrReadOnly


#user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

#class UserCreate(generics.ListCreateAPIView):
   # """ 
  #  Creates the user. 
 #   """
#
 #   def post(self, request, format='json'):
#    #    serializer = UserSerializer(data=request.data)
   #     if serializer.is_valid():
  #          user = serializer.save()
 #           if user:
#                return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreateView(generics.ListCreateAPIView):
	queryset = Gameslist.objects.all()
	serializer_class = GameslistSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)			

	def upload_pic(request):
		if request.method == 'POST':
			form = ImageUploadForm(request.POST, request.FILES)
			if form.is_valid():
				m = ExampleModel.objects.get(pk=course_id)
				m.game_pic = form.cleaned_data['image']
				m.save()
				return HttpResponse('image upload success')
		return HttpResponseForbidden('allowed only via POST')		

	#def perform_create(self, serializer):
	#	serializer.save(owner=self.request.user)
		
	#def createUser(request):
	#	user = User.objects.create_user(username='john',
     #                            email='jlennon@beatles.com',
      #                           password='glass onion')
		
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Gameslist.objects.all()
	serializer_class = GameslistSerializer
	permission_classes = (IsOwnerOrReadOnly,)
	#img_url=Gameslist.objects.filter(id=request.data['game_pic'])
	
	#img_url=upload_pic.objects.filter(id=request.data['id']) 

	#def upload_pic(request):
	#	upload_pic = open("staticfiles/", "rb").read()
	#	return HttpResponse(upload_pic, content_type="image/png")
	