from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = {
	url(r'^log/', include('rest_framework.urls',
		namespace='rest_framework')),
	url(r'^gameslists/$', CreateView.as_view(), name="create"),
	url(r'^gameslists/(?P<pk>[0-9]+)/$',
		DetailsView.as_view(), name="details"),
	#url(r'^$', views.index, name='index'),  #Render out HTML
	
	#url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
	#url(r'^staticfiles')
} 
#urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)