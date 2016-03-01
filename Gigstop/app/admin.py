from django.contrib import admin
from app.models import Performer, Event, Rating, Venue, Ticket, UserProfile, Like

admin.site.register(Performer)
admin.site.register(Event)
admin.site.register(Rating)
admin.site.register(Venue)
admin.site.register(Ticket)
admin.site.register(UserProfile)
admin.site.register(Like)
