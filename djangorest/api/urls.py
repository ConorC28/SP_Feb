from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView
from django.views.static import serve

from django.conf.urls import url, include
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

from django.contrib.auth.views import (
									login, 
									password_reset, 
									password_reset_done,
									password_reset_confirm,
									password_reset_complete
								)


from djangorest import urls

from djangorest.views import AddGames

urlpatterns = {
	url(r'^log/', include('rest_framework.urls',
		namespace='rest_framework')),
	url(r'^gameslists/$', CreateView.as_view(), name="create"),
	url(r'^gameslists/(?P<pk>[0-9]+)/$',
		DetailsView.as_view(), name="details"),
	url(r'^gameslists/$', CreateView.as_view(), name='gameslist'),
	
	#url(r'^', include('django.contrib.auth.urls')),
	url(r'^', include('djangorest.urls')),
	#(?P<uidb64>[a-z0-9]+)-(?P<token>.+)/$'
	url(r'^$',views.home, name='home'),
	url(r'home',views.home, name='home'),
	url(r'about',views.about, name='about'),
	url(r'news',views.news, name='news'),
	url(r'AddGames',AddGames.as_view(), name='AddGames'),
	url(r'gamescolpage',views.gamescolpage, name='gamescolpage'),
	url(r'login',login, {'template_name':'login.html'}),
	url(r'trends',views.trends, name='trends'),
	url(r'register',views.register, name='register'),
	url(r'welcome',views.welcome, name='welcome'),
	url(r'profile',views.profile, name='profile'),
	url(r'edit',views.edit, name='edit'),
	url(r'usergames',views.usergames, name='usergames'),
	url(r'changepassword',views.changepassword, name='changepassword'),
	url(r'resetpassword/$',password_reset, name='reset_password'),
	url(r'resetpassworddone/$',password_reset_done, name='password_reset_done'),
	url(r'resetpasswordconfirm/$',
	password_reset_confirm, name='password_reset_confirm(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$'),
	url(r'resetpasswordcomplete/$',password_reset_complete, name='password_reset_complete'),

	#(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$	
	
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