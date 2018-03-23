from django.conf.urls import url
from django.conf.urls.static import static
from cg import views
from djangorest import views
from api import urls
from django.conf.urls import url, include

urlpatterns = [
	
	url(r'^$',views.home, name='home'),
	url(r'home',views.home, name='home'),
	url(r'about',views.about, name='about'),
	url(r'news',views.news, name='news'),
	url(r'addgames',views.addgames, name='addgames'),
	url(r'trends',views.trends, name='trends'),
	
	#url(r'^', include('api.urls')),
	#url(r'^$',views.home, name='home'),
	#url(r'^about$',views.about, name='about'),
	#url(r'^about/$', views.AboutPageView.as_view()),
	
]