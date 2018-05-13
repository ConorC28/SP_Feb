from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateNewsView
from .views import CreateGameView
from .views import CreateArticleView
from .views import GameDetailsView
from .views import ArticleDetailsView
from .views import NewsDetailsView
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
from djangorest.views import AddArticles

urlpatterns = {
	url(r'^log/', include('rest_framework.urls',
		namespace='rest_framework')),
		
	url(r'^nlists/$', CreateNewsView.as_view(), name="createn"),
	url(r'^nlists/(?P<pk>[0-9]+)/$',
		NewsDetailsView.as_view(), name="detailsn"),
		
	url(r'^articleslists/$', CreateArticleView.as_view(), name="createa"),
	url(r'^articleslists/(?P<pk>[0-9]+)/$',
		ArticleDetailsView.as_view(), name="detailsa"),
		
	url(r'^gameslists/$', CreateGameView.as_view(), name="create"),
	url(r'^gameslists/(?P<pk>[0-9]+)/$',
		GameDetailsView.as_view(), name="detailsg"),
	
	url(r'^gameslists/$', CreateGameView.as_view(), name='gameslist'),
	
	url(r'^chat', views.chat),
	url(r'^ajax/chat/$', views.broadcast),
	
	
	
	url(r'^', include('djangorest.urls')),
	
	url(r'^$',views.home, name='home'),
	url(r'^home',views.home, name='home'),
	url(r'^about',views.about, name='about'),
	url(r'^news',views.news, name='news'),
	url(r'^AddGames$',AddGames.as_view(), name='AddGames'),
	url(r'^AddArticles$',AddArticles.as_view(), name='AddArticles'),
	url(r'^gamescol$',views.gamescol, name='gamescol'),
		url(r'^(?P<pk>\d+)$',views.oug, name='oug'),
	url(r'^userarticles',views.userarticles, name='userarticles'),
	url(r'^gamesdata',views.gamesdata, name='gamesdata'),
	url(r'^login',login, {'template_name':'login.html'}),
	url(r'^trends',views.trends, name='trends'),
	url(r'^register',views.register, name='register'),
	url(r'^welcome',views.welcome, name='welcome'),
	url(r'^profile$',views.profile, name='profile'),
		url(r'^editgame(?P<id>\d+)$',views.editgame, name='editgame'),
		url(r'^deletegame(?P<id>\d+)$',views.deletegame, name='deletegame'),
	url(r'^edit',views.edit, name='edit'),
	url(r'^usergames',views.usergames, name='usergames'),
	url(r'^password',views.changepassword, name='changepassword'),
	url(r'^resetpassword/$',password_reset, name='reset_password'),
	url(r'^resetpassworddone/$',password_reset_done, name='password_reset_done'),
	url(r'%resetpasswordconfirm/$',
	password_reset_confirm, name='password_reset_confirm(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$'),
	url(r'^resetpasswordcomplete/$',password_reset_complete, name='password_reset_complete'),
	url(r'^comments/', include('django_comments.urls')),
	
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
	url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
	
} 



urlpatterns = format_suffix_patterns(urlpatterns)