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


class NewEventForm(forms.ModelForm):

    # name = forms.CharField(max_length=128, unique=True)
    # time = forms.DateTimeField()
    # venue = forms.CharField(max_length=128)
    # media = forms.URLField(Label='YouTube link')
    # performer = forms.CharField(max_length=128, unique=True)
    performer =forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Event



# class NewEventTicketsForm(forms.ModelForm):
#     # price = forms.IntegerField()
#     # event = forms.ForeignKey(default="0")
#     # total = models.IntegerField()

#     class Meta:
#     	model = Ticket
#     	fields = ('price','event', 'sold')