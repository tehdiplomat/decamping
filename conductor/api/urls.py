from django.conf.urls import patterns, include, url

from conductor.api import *
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(BusResource())

urlpatterns = patterns('',
		('', include(v1_api.urls)),
	)