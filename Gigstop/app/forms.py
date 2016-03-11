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

class AddEventForm(forms.ModelForm):
	class Meta:
		model = Event
		exclude = ['performer']


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
