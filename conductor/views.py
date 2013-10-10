from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def index(request):
	return render_to_response("index.html", {
		
	}, RequestContext(request))