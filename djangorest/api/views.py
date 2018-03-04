from rest_framework import generics
from .serializers import GameslistSerializer
from .models import Gameslist
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateView(generics.ListCreateAPIView):
	queryset = Gameslist.objects.all()
	serializer_class = GameslistSerializer
	#permission_classes = (permissions.IsAuthenticated,)

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
		
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Gameslist.objects.all()
	serializer_class = GameslistSerializer
	#img_url=Gameslist.objects.filter(id=request.data['game_pic'])
