from django.test import TestCase
from app.models import Event,Venue,Performer,User
from datetime import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

def add_performer(bandname):
    tuser,created =User.objects.get_or_create(username = "test")
    tuser.save()
    p, created = Performer.objects.get_or_create(performer_id = tuser.id,bandname=bandname)
    p.save()
    return p

def add_event(time,media,venue,performer):
    e= Event.objects.get_or_create(time=time,media=media,venue=venue,performer=performer)
    e.save()
    return e

class CategoryMethodTests(TestCase):


    def test_One(self):

        tperformer = add_performer(bandname ="testband" )
        tvenue = Venue(name ="Stereo")
        tvenue.save()
        my_datetime = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
        event_one = Event(time =my_datetime,media='https://www.youtube.com/watch?v=eh7lp9umG2I',venue=tvenue,performer=tperformer,no_tickets=-1)
        event_one.save()
        self.assertEqual((event_one.no_tickets >=0),True)

    def test_two(self):

        self.assertEqual((1 >=0),True)


class ProfileViewTests(TestCase):

    def test_performer_has_no_event(self):

        p = add_performer("Isosceles")
        my_datetime = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
        tm = "https://www.youtube.com/watch?v=uH3zT03DkFQ"
        tvenue = Venue(name ="Stereo")
        tvenue.save()
        event_test = add_event(my_datetime,tm,tvenue,p)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)





