from django.db import models

from django.contrib import admin
#from django.contrib.auth.models import User

class Bus(models.Model):
	DECAMP_BROAD = "DC33M"
	DECAMP_GROVE = "DC33G"
	DECAMP_280X = "DC33X"
	DECAMP_88 = "DC88"

	ROUTE_CHOICES = (
		(DECAMP_BROAD, '33 Broad'),
		(DECAMP_GROVE, '33 Grove'),
		(DECAMP_280X, '33 280 Express'),
		(DECAMP_88, '88')
	)

	route = models.CharField(max_length=10, choices=ROUTE_CHOICES)
	inbound = models.BooleanField(default=True) # Inbound = Towards New York
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	lon = models.FloatField()
	lat = models.FloatField()

	def __unicode__(self):
		return self.route

	class Meta:
		app_label = 'conductor'
		ordering = ['route']
		verbose_name_plural = 'buses'

class BusAdmin(admin.ModelAdmin):
	fields = ['route', 'inbound']
