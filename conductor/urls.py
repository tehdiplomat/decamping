from django.conf.urls import patterns, include, url

urlpatterns = patterns('conductor.views',
	url(r'^$', 'index'),
	url(r'^index/', 'index'), 
)
