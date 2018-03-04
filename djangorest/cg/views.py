from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home(request):
	return render(
		request,
		'index.html',
		context = None)
		
def about(request):
	return render(
		request,
		'about.html',
		context = None)
""""class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None)
		
class AboutPageView(TemplateView):
	template_name = "about.html"
	#def get(self, request, **kwargs):
	#return render(request, 'about.html', context=None)
	"""
