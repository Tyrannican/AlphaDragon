import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gigstop.settings')

import django
from django.contrib.auth.models import User, Group
django.setup()

from app.models import Venue,Event,Performer

def populate():

    group = add_group("Band")

    kingtuts = add_venue("King Tut's Wah Wah Hut",'272a St Vincent St, Glasgow G2 5RL','0141 221 5279','Glasgow')


    Stereo = add_venue("Stereo",'22-28 Renfield Lane, Glasgow G2 5AR','0141 222 2254','Glasgow')


    Mono = add_venue("Mono",'12 Kings Court, Glasgow G1 5RB','0141 553 240054','Glasgow')
    Old_Fruitmarket  = add_venue("Old Fruitmarket",'Candleriggs, Glasgow G1 1NP','0141 353 8000','Glasgow')


    Kelvingrove_Bandstand  = add_venue("Kelvingrove Bandstand",'Kelvin Way, Glasgow G12 8NR','0141 276 9509','Glasgow')
    performer = add_performer('django1235','django@gmail.com','password','Django Django123','django@gmail.com','https://youtu.be/9bRR7yo-2UQ','Death Metal')

    Admiral_Fallow = add_performer('admiral','admiralfallow@gmail.com','password',"Admiral Fallow",'admiralfallow@gmail.com','https://youtu.be/oH9IDgyjr4E', 'Jazz')
    Frightened_Rabbit = add_performer('rabbit','frightenedrabit@gmail.com','password',"Frightened Rabbit",'frightenedrabit@gmail.com','https://youtu.be/k-YLMT6qqT4', 'Death Metal')
    Biffy_Clyro = add_performer('biffy','biffyclyro@gmail.com','password',"Biffy Clyro",'biffyclyro@gmail.com','https://youtu.be/YCG_yP5MsMc', 'Pop Rock')
    CHVRCHES = add_performer('chvrches','chvrches@gmail.com','password',"CHVRCHES",'chvrches@gmail.com','https://youtu.be/JyqemIbjcfg','Psychadelic Funk Rap')

    event1 = add_event('Celtic Connections',datetime.datetime(2016, 2, 28, 12, 26),Venue.objects.get(name="Stereo"),'',Performer.objects.get(bandname="Django Django123"))
    event2 = add_event('Gig Apocalypse',datetime.datetime(2016, 2, 27, 20, 30),Venue.objects.get(name="Mono"),'',Performer.objects.get(bandname="Admiral Fallow"))
    event3 = add_event('Fun in the Sun',datetime.datetime(2016, 2, 27, 20, 30),Venue.objects.get(name="Kelvingrove Bandstand"),'',Performer.objects.get(bandname="Biffy Clyro"))
    event4 = add_event('West End Festival',datetime.datetime(2016, 2, 26, 21, 30),Venue.objects.get(name="Old Fruitmarket"),'',Performer.objects.get(bandname="CHVRCHES"))
    event5 = add_event('Jazz Festival',datetime.datetime(2016, 2, 26, 21, 30),Venue.objects.get(name="King Tut's Wah Wah Hut"),'',Performer.objects.get(bandname="Frightened Rabbit"))




def add_event(name,time,venue,media,performer):
    c = Event.objects.get_or_create(name=name,time=time,venue=venue,performer=performer)

def add_venue(name,address,contact,location):
    c = Venue.objects.get_or_create(name=name,address=address,contact=contact,location=location)[0]
    print "Inserted "+name
    return c

def add_performer(username,email,password,bandname,paypal,media,genre):
    b = User.objects.get_or_create(username=username,email=email,password=password)
    b.set_password(password)
    b.save()
    perfomer_id = User.objects.get(username=username).id
    c = Performer.objects.get_or_create(performer_id=perfomer_id,bandname=bandname,paypal=paypal,media=media,genre=genre)

    print "Inserted "+bandname
    return c

def add_group(name):
    g = Group.objects.get_or_create(name=name)
    print "Created Band Group"
    return g

if __name__ == '__main__':
    print "Starting GigStop population script..."
    populate()