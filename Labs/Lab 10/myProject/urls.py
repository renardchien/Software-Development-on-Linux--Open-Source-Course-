from django.conf.urls.defaults import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    url(r'^boards/', include('messageboards.urls')),
    #url(r'.*', include('messageboards.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
	(r'^uploaded/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root':	settings.MEDIA_ROOT}),
)

urlpatterns += patterns('',
	url(r'^$', include('messageboards.urls')),
)
