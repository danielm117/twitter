from django.shortcuts import render
from django.template import loader, Context, RequestContext
from twitterApp.models import Profile
from django.http import HttpResponse

import os


# Create your views here.

def home(request):
	profile = Profile.objects.get(pk=1)
	template = loader.get_template("home.html")
	context = RequestContext(request,{'perfil':profile})
	return HttpResponse({template.render(context)})



