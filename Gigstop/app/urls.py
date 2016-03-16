from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^user_registration/$', views.user_reg, name='user_registration'),
	url(r'^performer_registration/$', views.performer_reg, name='performer_registration'),
	url(r'^add_event/$', views.add_event, name='add_event'),
	url(r'^performer_profile/$', views.performer_profile, name='performer_profile'),
	url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
	url(r'^edit_event/(?P<event_name_slug>[\w\-]+)/$', views.delete_event, name='delete_event'),
	url(r'^edit_event/$', views.edit_event, name='edit_event'),
	url(r'^buy_tickets/(?P<event_name_slug>[\w\-]+)/$', views.buy_tickets, name='buy_tickets'),
	url(r'^thanks/$', views.thanks, name='thanks')
	)