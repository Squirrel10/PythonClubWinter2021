from django.shortcuts import render, get_object_or_404
from . models import Meetings, Resource, Event
from django.urls import reverse_lazy 
from .forms import MeetingsForm


# Create your views here.
def index(request): 
    return render(request, 'Club/index.html')

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'Club/resource.html', {'resource_list' : resource_list})

def meetings(request, id): 
    meeting=get_object_or_404(Meetings, pk=id)
    return render(request, 'Club/meeting.html', {'meeting' : meeting})


def newProduct(request): 
    form=MeetingsForm

    if request.method=='POST':
        form = MeetingsForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingsForm()
    else:
        form=MeetingsForm()
    return render(request, 'Club/newmeeting.html', {'form' : form})

