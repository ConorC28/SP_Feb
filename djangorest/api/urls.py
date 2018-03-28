from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView
from django.views.static import serve


											#Imports do display images, static files
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import StaticFilesStorage

from . import views
from djangorest import views
from django.contrib.staticfiles.storage import StaticFilesStorage
from djangorest import views
from djangorest import urls
from django.views.generic import TemplateView
from django.conf import settings

from djangorest import urls


urlpatterns = {
	url(r'^log/', include('rest_framework.urls',
		namespace='rest_framework')),
	url(r'^gameslists/$', CreateView.as_view(), name="create"),
	url(r'^gameslists/(?P<pk>[0-9]+)/$',
		DetailsView.as_view(), name="details"),
	url(r'^gameslists/$', CreateView.as_view(), name='gameslist'),
	
	url(r'^$',views.home, name='home'),
	url(r'home',views.home, name='home'),
	url(r'about',views.about, name='about'),
	url(r'news',views.news, name='news'),
	url(r'addgames',views.addgames, name='addgames'),
	url(r'trends',views.trends, name='trends'),

	
	#url(r'^gameslists/(?P<pk>[0-9]+)/staticfiles/$'),
	
	#path('../cd/templates/addgames.html', TemplateView.as_view(template_name=addgames.html)),
		
	#url(r'^users/', include('api.urls')),
	

	#url(r'^$', views.index, name='index'),  #Render out HTML
	
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
	url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
	#url(r'^staticfiles')
} 


#urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)