from django.http import HttpResponse
from django.shortcuts import render
from app.models import Performer, Event, Rating, Venue, Ticket, User, Like

def index(request):
	context_dict = {}
	return render(request, 'Gigstop/wall.html', context_dict)
