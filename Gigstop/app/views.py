from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.models import Performer, Event, Rating, Venue, Ticket, User, Like

def index(request):
	context_dict = {}
	return render(request, 'Gigstop/index.html', context_dict)

def about(request):
	return render(request, 'Gigstop/about.html', {})

def login(request):
	#POST
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('pass')
		user = authenticate(username=username, password = password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/app/')
			else:
				return HttpResponse('Your Gigstop account is disabled')
		else:
			print "Invalid login details supplied {0}, {1}".format(username, password)
			return HttpResponse('Invalid login details supplied')
	#GET
	else:
		return render(request, 'Gigstop/login.html', {})

@login_required
def logout(request):
	logout(request)

	return HttpResponseRedirect('/app/')

