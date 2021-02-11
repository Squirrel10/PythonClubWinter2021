from django.shortcuts import render
from . models import Meetings, Resource, Event
# Create your views here.
def index(request): 
    return render(request, 'Club/index.html')

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'Club/resource.html', {'resource_list' : resource_list})

