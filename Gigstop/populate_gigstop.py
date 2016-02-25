import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gigstop.settings')

import django
django.setup()

from app.models import Venue,Event,Performer

def populate():
    kingtuts = add_venue("King Tut's Wah Wah Hut",'272a St Vincent St, Glasgow G2 5RL','0141 221 5279','Glasgow')


    Stereo = add_venue("Stereo",'22-28 Renfield Lane, Glasgow G2 5AR','0141 222 2254','Glasgow')


    Mono = add_venue("Mono",'12 Kings Court, Glasgow G1 5RB','0141 553 240054','Glasgow')


    Kelvingrove_Bandstand  = add_venue("Kelvingrove Bandstand",'Kelvin Way, Glasgow G12 8NR','0141 276 9509','Glasgow')


    Old_Fruitmarket  = add_venue("Old Fruitmarket",'Candleriggs, Glasgow G1 1NP','0141 353 8000','Glasgow')

    Django_Django = add_performer("Django Django",'django','django@gmail.com','django@gmail.com','https://youtu.be/9bRR7yo-2UQ')

    Admiral_Fallow = add_performer("Admiral Fallow",'admiral','admiralfallow@gmail.com','admiralfallow@gmail.com','https://youtu.be/oH9IDgyjr4E')

    Frightened_Rabbit = add_performer("Frightened Rabbit",'rabbit','frightenedrabit@gmail.com','frightenedrabit@gmail.com','https://youtu.be/k-YLMT6qqT4')

    Biffy_Clyro = add_performer("Biffy Clyro",'biffy','biffyclyro@gmail.com','biffyclyro@gmail.com','https://youtu.be/YCG_yP5MsMc')

    CHVRCHES = add_performer("CHVRCHES",'chvrches','chvrches@gmail.com','chvrches@gmail.com','https://youtu.be/JyqemIbjcfg')

    event1 = add_event('Celtic Connections',datetime.datetime(2016, 2, 28, 12, 26),Venue.objects.get(name="Stereo"),'',Performer.objects.get(name="Django Django"))
    event2 = add_event('Gig Apocalypse',datetime.datetime(2016, 2, 27, 20, 30),Venue.objects.get(name="Mono"),'',Performer.objects.get(name="Admiral Fallow"))
    event3 = add_event('Fun in the Sun',datetime.datetime(2016, 2, 27, 20, 30),Venue.objects.get(name="Kelvingrove Bandstand"),'',Performer.objects.get(name="Biffy Clyro"))
    event4 = add_event('West End Festival',datetime.datetime(2016, 2, 26, 21, 30),Venue.objects.get(name="Old Fruitmarket"),'',Performer.objects.get(name="CHVRCHES"))
    event5 = add_event('Jazz Festival',datetime.datetime(2016, 2, 26, 21, 30),Venue.objects.get(name="King Tut's Wah Wah Hut"),'',Performer.objects.get(name="Frightened Rabbit"))




def add_event(name,time,venue,media,performer):
    c = Event.objects.get_or_create(name=name,time=time,venue=venue,performer=performer)

def add_venue(name,address,contact,location):
    c = Venue.objects.get_or_create(name=name,address=address,contact=contact,location=location)[0]
    print "Inserted"+name
    return c

def add_performer(name,username,email,paypal,media):
    c = Performer.objects.get_or_create(name=name,username=username,email=email,paypal=paypal,media=media)
    print "Inserted"+name
    return c
if __name__ == '__main__':
    print "Starting GigStop population script..."
    populate()