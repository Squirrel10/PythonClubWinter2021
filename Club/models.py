from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meetings(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.CharField(max_length=255)
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.CharField(max_length=255)
  # typedescription=models.TextField(null=True, blank=True)


    def __str__(self):
        return self.typename
        
    class Meta:
        db_table='meetings'

class MeetingMinutes(models.Model):
    meetingminutesid=models.ForeignKey(Meetings, on_delete=models.DO_NOTHING)
    attendance=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    minutes=models.CharField(max_length=255)



    def __str__(self):
        return self.meetingminutes

    class Meta:
        db_table='meetingmintes'

class Resource(models.Model):
    resourcetitle=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField()
    reviewdate=models.DateField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    resourcedescription=models.TextField()

 
    def __str__(self):
        return self.Resource

    class Meta: 
        db_table='resource'
    
class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventstime=models.CharField(max_length=255)
    eventdescription=models.TextField()
    eventdate=models.DateField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Event

    class Meta: 
        db_table='event'



    