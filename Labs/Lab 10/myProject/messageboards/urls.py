from django.conf.urls.defaults import *

urlpatterns = patterns('messageboards.views',
	(r'^$', 'login'),
	(r'^register/$', 'register'),
	(r'^create/$', 'create'),
	(r'^createthread/$', 'createThread'),
	(r'^page/(?P<inpage>[\sA-Za-z0-9]+)/(#bottom)?$', 'messages'),
	(r'.*', 'default'),
)


