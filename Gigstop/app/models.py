from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=256)
    contact = models.CharField(max_length=256)
    location = models.CharField(max_length=128)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name


class UserProfile(models.Model):

    user = models.OneToOneField(User, null=True)
    location = models.CharField(max_length=128)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.user.username

class Performer (models.Model):
    performer = models.ForeignKey(User, null=True)
    paypal = models.CharField(max_length=128)
    media = models.URLField()
    genre = models.CharField(max_length=128)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.performer.username

class Event(models.Model):
	
    name = models.CharField(max_length=128, unique=True)
    time = models.DateTimeField()
    venue = models.ForeignKey(Venue)
    media = models.URLField()
    performer = models.ForeignKey(Performer)
	

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name


class Ticket(models.Model):
    price = models.IntegerField(max_length=100000)
    event = models.ForeignKey(Event)
    sold = models.IntegerField(max_length=1)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.price
		
class Rating (models.Model):
    user = models.ForeignKey(User)
    performer = models.ForeignKey(Performer)
    type = models.CharField(max_length=24)
    Date = models.CharField(max_length=24)
    Rating = models.IntegerField(max_length=2)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.type


class Like(models.Model):
    user = models.ForeignKey(User)
    performer = models.ForeignKey(Performer)
    
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.user


