from django import forms
from app.models import Event, Rating, Performer, Venue, Ticket, UserProfile, Like
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('location',)

class AddEventForm(forms.Form):
    name = forms.CharField( required=True)

    Media = forms.URLField(required = False)
    eventDate = forms.DateField(required=True)
    eventTime =forms.TimeField(required=True)
    venueName = forms.CharField(required=True)
    address = forms.CharField(required=True)
    contact = forms.CharField(required=True)
    location = forms.CharField(required=True)
    no_tickets = forms.IntegerField()

    class Meta:
		fields = ('name','eventDate','eventTime','VenueName', 'Media',)


class NewEventTicketsForm(forms.ModelForm):
    price = forms.IntegerField()
    event = forms.CharField(widget=forms.HiddenInput(), required=False)
    sold = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
    	model = Ticket
    	fields = ('price','event', 'sold')




class PerformerProfileForm(forms.ModelForm):
    class Meta:
        model = Performer
        fields = ('bandname', 'paypal', 'media', 'genre')
