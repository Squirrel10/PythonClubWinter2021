from django.test import TestCase
from django.contrib.auth.models  import User
from .models import Resource, MeetingMinutes, Meetings, Event
import datetime

class MeetingsTest(TestCase):
    def setUp(self):
        self.type=Meetings(meetingtitle= 'test')



    def test_typestring(self):
        self.assertEqual(str(self.type), 'test')


    def test_tablename(self):
        self.assertEqual(str(Meetings._meta.db_table), 'meetings') 


class ResourceTest(TestCase): 
    def setUp(self): 
        self.type=Meetings(meetingtitle= 'test_name')
        self.user=User(username='user1')
        self.resource=Resource(resourcename='Lenovo', resourcetype=self.type, user=self.user, reviewdate=datetime.date(2021,1,10), resourceprice=1200.99, resourceurl='http://www.lenovo.com', resourcedescription="lenovo laptop")   

    
    def test_string(self):
        self.assertEqual(str(self.resource), 'Lenovo')

    def test_discount(self):
        disc = self.resource.resourceprice * .05
        self.assertEqual(self.resource.discountAmount(), disc)


    def test_discountAmount(self):
        disc=self.resouce.resourceprice * (1 -.05)
        self.assertEqual(self.resource.discountPrice(),disc)
        

