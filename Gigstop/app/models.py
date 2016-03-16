from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Venue(models.Model):
    name = models.CharField(max_length=128)
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
    bandname = models.CharField(max_length=128,null=False)
    paypal = models.CharField(max_length=128)
    media = models.URLField()
    genre = models.CharField(max_length=128)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.bandname

class Event(models.Model):
	
        name = models.CharField(max_length=128, unique=True)
        time = models.DateTimeField()
        venue = models.ForeignKey(Venue)
        media = models.URLField()
        performer = models.ForeignKey(Performer)
        slug = models.SlugField()
        no_tickets = models.IntegerField(default=0)
        price = models.IntegerField(default=0)

        def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Event, self).save(*args, **kwargs)

        def __unicode__(self):  #For Python 2, use __str__ on Python 3
            return self.name


class Ticket(models.Model):
    price = models.IntegerField(max_length=100000)
    event = models.ForeignKey(Event)
    user = models.ForeignKey(User)
    quantity = models.IntegerField(max_length=3)

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


