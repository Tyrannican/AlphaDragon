import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gigstop.settings')

import django
from django.contrib.auth.models import User, Group
django.setup()

from app.models import Venue,Event,Performer,UserProfile,Ticket

def populate():

    group = add_group("Band")
#Add Venues
    kingtuts = add_venue("King Tut's Wah Wah Hut",'272a St Vincent St, Glasgow G2 5RL','0141 221 5279','Glasgow')
    Stereo = add_venue("Stereo",'22-28 Renfield Lane, Glasgow G2 5AR','0141 222 2254','Glasgow')
    Mono = add_venue("Mono",'12 Kings Court, Glasgow G1 5RB','0141 553 240054','Glasgow')
    Old_Fruitmarket  = add_venue("Old Fruitmarket",'Candleriggs, Glasgow G1 1NP','0141 353 8000','Glasgow')
    Kelvingrove_Bandstand  = add_venue("Kelvingrove Bandstand",'Kelvin Way, Glasgow G12 8NR','0141 276 9509','Glasgow')
    bannersmans = add_venue("Bannerman's Bar",'202 Cowgate, Edinburgh EH1 1NQ','0131 556 3254','Edinburgh')
    whistlebinkies = add_venue("Whistlebinkies Live Music Bar",'4-6 South Bridge, Edinburgh EH1 1LL','0131 557 5114','Edinburgh')
    finnegans = add_venue("Finnegan's Wake",'9B Victoria St, Edinburgh EH1 2HE','0131 225 9348','Edinburgh')
    thecaves = add_venue("The Caves",'8-12 Niddry St S, Edinburgh EH1 1NS','0131 510 6969','Edinburgh')
    voltaire = add_venue("Cabaret Voltaire",'36-38 Blair St, Edinburgh EH1 1QR','0131 247 4704','Edinburgh')
    liquidrooms = add_venue("The Liquid Rooms",'9c Victoria Street, Edinburgh EH1 2HE','0131 225 2564','Edinburgh')
    windmill = add_venue("Windmill Brixton",'22 Blenheim Gardens, London SW2 5BZ','020 8671 0700','London')
    borderline = add_venue("The Borderline",'Orange Yard, Manette St, London W1D 4JB','020 7734 5547','London')
    roundhouse = add_venue("Roundhouse",'Chalk Farm Rd, London NW1 8EH','0300 678 9222','London')
    vortex = add_venue("Vortex",'11 Gillett Square, London N16 8AZ','020 7254 4097','London')
    cavendish = add_venue("The Cavendish Arms",'128 Hartington Rd, London SW8 2HJ','020 7498 7464','London')
    tolbooth = add_venue("The Tolbooth",'Jail Wynd, Stirling FK8 1DE','01786 274000','Stirling')
    kangeroo = add_venue("Kilted Kangaroo",'9 Upper Craigs, Stirling FK8 2DG','01786 451130','Stirling')
    molly = add_venue("Molly Malones",'11 Maxwell Pl, Stirling FK8 1JU','01786 478264','Stirling')
    alberthalls = add_venue("Albert Halls",'Albert Place, Dumbarton Rd, Stirling FK8 2QL','01786 473544','Stirling')
    behindthewall = add_venue("Behind The Wall",'14 Melville St, Falkirk, Stirlingshire FK1 1HZ','01324 633338','Stirling')
    thetunnels = add_venue("The Tunnels","Carnegie's Brae, Aberdeen, Aberdeen City AB10 1BF",'01224 211121','Aberdeen')
    krakatoa = add_venue("Krakatoa","2 Trinity Quay, Aberdeen AB11 5AA",'01224 587602','Aberdeen')
    bluelamp = add_venue("Blue Lamp","121 Gallowgate, Aberdeen AB25 1BU",'01224 647472','Aberdeen')
    drummonds = add_venue("Cafe Drummonds","1 Belmont St, Aberdeen, Grampian AB10 1JR",'01224 619930','Aberdeen')
    lemontree = add_venue("The Lemon Tree","5 W N St, Aberdeen AB24 5AT",'01224 337688','Aberdeen')

#Add Performers
    performer = add_performer('django1235','django@gmail.com','password','Django Django','django@gmail.com','https://www.youtube.com/watch?v=9bRR7','Death Metal')
    Admiral_Fallow = add_performer('admiral','admiralfallow@gmail.com','password',"Admiral Fallow",'admiralfallow@gmail.com','https://www.youtube.com/watch?v=oH9IDgyjr4E', 'Folk')
    Frightened_Rabbit = add_performer('rabbit','frightenedrabit@gmail.com','password',"Frightened Rabbit",'frightenedrabit@gmail.com','https://www.youtube.com/watch?v=k-YLMT6qqT4', 'Death Metal')
    Biffy_Clyro = add_performer('biffy','biffyclyro@gmail.com','password',"Biffy Clyro",'biffyclyro@gmail.com','https://www.youtube.com/watch?v=YCG_yP5MsMc', 'Pop Rock')
    CHVRCHES = add_performer('chvrches','chvrches@gmail.com','password',"CHVRCHES",'chvrches@gmail.com','https://www.youtube.com/watch?v=JyqemIbjcfg','Psychadelic Funk Rap')
    cascada = add_performer('cascada','cascada@gmail.com','password','Cascada','cascada@gmail.com','https://www.youtube.com/watch?v=k7JTClfWtTQ','Rock')
    wethesame = add_performer('wethesame','wethesame@gmail.com','password','We, The Same','wethesame@gmail.com','https://www.youtube.com/watch?v=7tgIVjNLcdk','Rock')
    saw = add_performer('saw','saw@gmail.com','password','The Saw','saw@gmail.com','https://www.youtube.com/watch?v=Y49hSneTY-w','Rock')
    flynn = add_performer('flynn','flynn@gmail.com','password','Johnny Flynn','flynn@gmail.com','https://www.youtube.com/watch?v=vbksyHcGsx0','Folk')
    benders = add_performer('benders','benders@gmail.com','password','The Morning Benders','benders@gmail.com','https://www.youtube.com/watch?v=vbksyHcGsx0','Folk')
    lianne = add_performer('lianne','liannelahavas@gmail.com','password','Lianne La Havas','liannelahavas@gmail.com','https://www.youtube.com/watch?v=vbksyHcGsx0','Folk')

#Add Events
    event1 = add_event('Celtic Connections',datetime.datetime(2016, 3, 28, 12, 26),Venue.objects.get(name="Stereo"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Django Django"),40, 8)
    event2 = add_event('Gig Apocalypse',datetime.datetime(2016, 3, 27, 20, 30),Venue.objects.get(name="Mono"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Admiral Fallow"),25, 7.50)
    event3 = add_event('Fun in the Sun',datetime.datetime(2016, 3, 27, 20, 30),Venue.objects.get(name="Kelvingrove Bandstand"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Biffy Clyro"),100, 40)
    event4 = add_event('West End Festival',datetime.datetime(2016, 3, 26, 21, 30),Venue.objects.get(name="Old Fruitmarket"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="CHVRCHES"), 50, 10)
    event5 = add_event('Jazz Festival',datetime.datetime(2016, 3, 26, 21, 30),Venue.objects.get(name="King Tut's Wah Wah Hut"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Frightened Rabbit"), 50, 12.50)

    event11 = add_event('Celtic Connections',datetime.datetime(2016, 3, 28, 13, 15),Venue.objects.get(name="Stereo"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Cascada"),20, 2)
    event22 = add_event('Gig Apocalypse',datetime.datetime(2016, 3, 27, 20, 30),Venue.objects.get(name="Mono"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="We, The Same"),25, 7.50)
    event33 = add_event('Fun in the Sun',datetime.datetime(2016, 3, 27, 20, 00),Venue.objects.get(name="Kelvingrove Bandstand"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Johnny Flynn"),80, 15)
    event44 = add_event('West End Festival',datetime.datetime(2016, 3, 26, 22, 30),Venue.objects.get(name="Old Fruitmarket"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="The Morning Benders"), 70, 17)
    event55 = add_event('Jazz Festival',datetime.datetime(2016, 3, 26, 19, 30),Venue.objects.get(name="King Tut's Wah Wah Hut"),'',Performer.objects.get(bandname="Lianne La Havas"), 50, 12.50)

    london10 = add_event('Junction 2',datetime.datetime(2016, 3, 25, 19, 15),Venue.objects.get(name="Windmill Brixton"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Django Django"),40, 8)
    london12 = add_event('Born & Bred',datetime.datetime(2016, 3, 28, 20, 30),Venue.objects.get(name="Roundhouse"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Admiral Fallow"),25, 7.50)
    london13 = add_event('Meltdown',datetime.datetime(2016, 3, 28, 20, 30),Venue.objects.get(name="Vortex"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Biffy Clyro"),100, 40)
    london14 = add_event('Field Day',datetime.datetime(2016, 3, 27, 21, 30),Venue.objects.get(name="The Borderline"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="CHVRCHES"), 50, 10)
    london15 = add_event('Raw Power',datetime.datetime(2016, 3, 27, 21, 30),Venue.objects.get(name="Cabaret Voltaire"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Frightened Rabbit"), 50, 12.50)

    london20 = add_event('Junction 2',datetime.datetime(2016, 3, 25, 20, 15),Venue.objects.get(name="Windmill Brixton"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Cascada"),40, 8)
    london22 = add_event('Born & Bred',datetime.datetime(2016, 3, 28, 21, 30),Venue.objects.get(name="Roundhouse"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="We, The Same"),25, 7.50)
    london23 = add_event('Meltdown',datetime.datetime(2016, 3, 28, 21, 30),Venue.objects.get(name="Vortex"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="The Morning Benders"),100, 40)
    london24 = add_event('Field Day',datetime.datetime(2016, 3, 27, 22, 30),Venue.objects.get(name="The Borderline"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="CHVRCHES"), 50, 10)
    london25 = add_event('Raw Power',datetime.datetime(2016, 3, 27, 22, 30),Venue.objects.get(name="Cabaret Voltaire"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Lianne La Havas"), 50, 12.50)

    edinburgh1 = add_event('From The Jam',datetime.datetime(2016, 4, 1, 20, 15),Venue.objects.get(name="The Liquid Rooms"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Biffy Clyro"),40, 8)
    edinburgh2 = add_event('Hosting the Masquerade"',datetime.datetime(2016, 4, 2, 21, 30),Venue.objects.get(name="The Caves"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="We, The Same"),25, 7.50)
    edinburgh3 = add_event('Excuses',datetime.datetime(2016, 3, 31, 21, 30),Venue.objects.get(name="Bannerman's Bar"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="The Morning Benders"),100, 40)
    edinburgh4 = add_event('Lianne La Havas Plays',datetime.datetime(2016, 3, 30, 22, 30),Venue.objects.get(name="Cabaret Voltaire"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Lianne La Havas"), 50, 10)
    edinburgh5 = add_event('Squealing Pigs',datetime.datetime(2016, 4, 2, 22, 30),Venue.objects.get(name="Cabaret Voltaire"),'https://www.youtube.com/watch?v=eh7lp9umG2I',Performer.objects.get(bandname="Admiral Fallow"), 50, 12.50)

#Add Users
    leif = add_user('leif','leif.azzopardi@glasgow.ac.uk','leif','Glasgow')
    laura = add_user('laura','laura@glasgow.ac.uk','laura','Glasgow')
    david = add_user('david','david@glasgow.ac.uk','david','Glasgow')
    patrick = add_user('patrick','9500143G@student.gla.ac.uk','patrick','Glasgow')
    graham = add_user('graham','grahamkeenan@hotmail.co.uk','graham','Glasgow')
    chris = add_user('chris','christopher.melville@me.com','chris','Glasgow')

#Add Tickets
    addtickets = insert_tickets(User.objects.get(username='patrick'),2)
    addtickets = insert_tickets(User.objects.get(username='leif'),1)
    addtickets = insert_tickets(User.objects.get(username='laura'),2)
    addtickets = insert_tickets(User.objects.get(username='david'),3)
    addtickets = insert_tickets(User.objects.get(username='graham'),4)
    addtickets = insert_tickets(User.objects.get(username='chris'),5)




def add_event(name,time,venue,media,performer,no_tickets,price):
    performermedia = performer.media
    c = Event.objects.get_or_create(name=name,time=time,venue=venue,media=performermedia,performer=performer,no_tickets=no_tickets,price=price)


def add_venue(name,address,contact,location):
    c = Venue.objects.get_or_create(name=name,address=address,contact=contact,location=location)[0]
    print "Inserted "+name
    return c

def add_performer(username,email,password,bandname,paypal,media,genre):
    b, created = User.objects.get_or_create(username=username,email=email,password=password)
    b.set_password(password)
    b.save()
    perfomer_id = User.objects.get(username=username).id
    c = Performer.objects.get_or_create(performer_id=perfomer_id,bandname=bandname,paypal=paypal,media=media,genre=genre)
    group = Group.objects.get(name='Band')
    b.groups.add(group)

    print "Inserted "+bandname
    return c

def add_group(name):
    g = Group.objects.get_or_create(name=name)
    print "Created Band Group"
    return g


def add_user(username,email,password,location):
    b, created = User.objects.get_or_create(username=username,email=email,password=password)
    b.set_password(password)
    b.save()
    thisuser = User.objects.get(username=username)
    c = UserProfile.objects.get_or_create(user=thisuser,location=location)
    return c

def insert_tickets(user,no_tickets):
        events = Event.objects.all()
        for e in events:
            ticket = Ticket()
            ticket.event = e
            ticket.price = e.price
            ticket.quantity = no_tickets
            ticket.user = User.objects.get(username=user.username)
            ticket.save()






if __name__ == '__main__':
    print "Starting GigStop population script..."
    populate()