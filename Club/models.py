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
        return self.meetingtitle
        
    class Meta:
        db_table='meetings'

class MeetingMinutes(models.Model):
    meetingminutesid=models.ForeignKey(Meetings, on_delete=models.DO_NOTHING)
    attendance=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    minutes=models.CharField(max_length=255)



    def __str__(self):
        return self.minutes

    class Meta:
        db_table='meetingmintes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField()
    reviewdate=models.DateField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    resourcedescription=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)

    def discountAmount(self):
        self.discount=self.resourceprice * .05
        return self.discount

#need to figure out why it's not working
#something to do with the function itself

    def discountPrice(self):
        disc=self.discountAmount()
        self.discountedPrice=self.resourceprice-disc    

 
    def __str__(self):
        return self.resourcename

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
        return self.eventtitle

    class Meta: 
        db_table='event'



    