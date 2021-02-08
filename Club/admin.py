from django.contrib import admin
from .models import Meetings, MeetingMinutes, Resource, Event

admin.site.register(Meetings)
admin.site.register(MeetingMinutes)
admin.site.register(Resource)
admin.site.register(Event)
