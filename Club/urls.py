from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path ('resource/', views.resources, name= 'resource'),
 path ('meetingdetail/<int:id>', views.meetings, name="meetingdetail" ),
 path ('newmeeting/',views.newProduct, name='newmeeting'),
 path ('loginmessage/', views.loginmessage, name='loginmessage'),
 path ('logoutmessage/', views.logoutmessage, name='logoutmessage'),

]
