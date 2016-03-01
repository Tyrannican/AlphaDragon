from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.forms import UserForm, UserProfileForm
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


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'Gigstop/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )



