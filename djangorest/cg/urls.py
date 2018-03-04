from django.conf.urls import url
from cg import views

urlpatterns = [
	url(r'^$',views.home, name='home'),
	url(r'^about$',views.about, name='about'),
	#url(r'^about/$', views.AboutPageView.as_view()),
]