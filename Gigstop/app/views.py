from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, user_passes_test
from app.forms import UserForm, UserProfileForm, AddEventForm, NewEventTicketsForm, PerformerProfileForm, PurchaseTicketForm
from app.models import Performer, Event, Rating, Venue, Ticket, User, Like
from django.template import loader, RequestContext
from datetime import datetime ,date , time

#Index page view
def index(request):
	

    wallPopulate = Event.objects.order_by('-time')
    template = loader.get_template('Gigstop/index.html')
    context = RequestContext(request, {'wallPopulate':wallPopulate,})

    # context_dict = {'Event':event}

    return HttpResponse(template.render(context))
    # return render(request, 'Gigstop/index.html')

#About page vew
def about(request):
	return render(request, 'Gigstop/about.html', {})

#user login view
def user_login(request):
	#POST
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('pass')
		user = authenticate(username=username, password = password)

		if user:
			if user.is_active:
				login(request, user)
                                if is_member(user)==True:
                                    return HttpResponseRedirect('/app/performer_profile/')
				return HttpResponseRedirect('/app/')
			else:
				return HttpResponse('Your Gigstop account is disabled')
		else:
			print "Invalid login details supplied {0}, {1}".format(username, password)
			return HttpResponse('Invalid login details supplied')
	#GET
	else:
		return render(request, 'Gigstop/login.html', {})

#checks to see if a User is a band or not
def is_member(user):
    return user.groups.filter(name='Band').exists()

#Logout view
@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/app/')

#Register view
def register(request):
    return render(request, 'Gigstop/register.html', {})
   
#User registration view
def user_reg(request):
     # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'Gigstop/user_registration.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )



#Performer registration view
def performer_reg(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = PerformerProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            group = Group.objects.get(name='Band')
            user.groups.add(group)

            profile = profile_form.save(commit=False)
            profile.performer = user
            profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = PerformerProfileForm()

    return render(request,
        'Gigstop/performer_registration.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


#Add event view for Performers only
def add_event(request):
    if request.method == 'POST':
        event_form = AddEventForm(data=request.POST)

        if event_form.is_valid():
            event = Event()
            event.name =event_form.cleaned_data['name']
            dT = datetime.combine(event_form.cleaned_data['eventDate'], event_form.cleaned_data['eventTime'])
            event.time = dT
            event.no_tickets = event_form.cleaned_data['no_tickets']
            vname = event_form.cleaned_data['venueName']
            vAddress = event_form.cleaned_data['address']
            vcontact = event_form.cleaned_data['contact']
            vlocation =event_form.cleaned_data['location']

            try:
            	v = Venue.objects.get(name=vname)
            except:
				v = Venue.objects.create(name=vname,address=vAddress,contact=vcontact,location=vlocation)
            event.venue = v
            get_performer = User.objects.get(username=request.user.username)
            performer = Performer.objects.get(performer=get_performer)
            event.performer = performer
            event.save()

            return HttpResponseRedirect('/app/performer_profile/')

        else:
            print event_form.errors
    else:
        event_form = AddEventForm()

    return render(request, 'Gigstop/add_event.html', {'event_form': event_form})

#Select event to edit event view for Performers only
@login_required
def edit_event(request):
    get_performer = User.objects.get(username=request.user.username)
    performer = Performer.objects.get(performer=get_performer)
    event_performer = Event.objects.all().filter(performer=performer)

    return render(request, 'Gigstop/edit_event.html', {'event': event_performer})

#Delete event view for Performers
@login_required
def delete_event(request, event_name_slug):
    delete = Event.objects.get(slug=event_name_slug)
    delete.delete()

    return HttpResponseRedirect('/app/edit_event/')

#Performer profile page view
def performer_profile(request):
    get_performer = User.objects.get(username=request.user.username)
    performer = Performer.objects.get(performer=get_performer)
    event_performer = Event.objects.all().filter(performer=performer)
    bandname = performer.bandname
    context_dict = {'events': event_performer}
    context_dict['bandname']= bandname
    return render(request, 'Gigstop/performer_profile.html',context_dict )

#Edit performer profile page view
def edit_profile(request):
    return render(request, 'Gigstop/edit_profile.html', {})


#Purchase Tickets view
def buy_tickets(request, event_id):
    event = Event.objects.get(id=event_id)

    if request.method == 'POST':
        buy_form = PurchaseTicketForm(data=request.POST)

        if buy_form.is_valid:
            ticket = buy_form.save(commit=False)
            ticket.event = event
            ticket.price = event.price
            ticket.user = User.objects.get(username=request.user.username)
            ticket.save()

            decrement = ticket.quantity
            no_tickets = event.no_tickets
            newTickets = Event.objects.filter(id=event_id).update(no_tickets=no_tickets-decrement)
            return HttpResponseRedirect('/app/thanks/')
        else:
            print buy_form.errors
    else:
        buy_form = PurchaseTicketForm()

    return render(request, 'Gigstop/buy_tickets.html', {'event': event, 'buy_form': buy_form})


#Thank you view
def thanks(request):
    return render(request, 'Gigstop/thanks.html', {})

def show_tickets(request,event_id):
    list_of_tickets = Ticket.objects.filter(event_id=event_id)
    return render(request,'Gigstop/showtickets.html', {'tickets': list_of_tickets})