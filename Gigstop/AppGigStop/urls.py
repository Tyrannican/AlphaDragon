from django.conf.urls import patterns, url
from AppGigStop import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'))