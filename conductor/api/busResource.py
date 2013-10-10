from tastypie.resources import ModelResource
from tastypie import fields
from conductor.models import Bus
from tastypie.authorization import Authorization

class BusResource(ModelResource):

	class Meta:
		queryset = Bus.objects.all()
		resource_name = 'bus'
		authorization = Authorization()  # TODO: real authorization
		always_return_data = True
		include_resource_uri = False

	def dehydrate(self, bundle):
		bundle.data['id'] = int(bundle.data['id'])
		return bundle

	def hydrate(self, bundle):
		if not bundle.obj.id:
			bundle.obj.creator = bundle.request.user

		return bundle