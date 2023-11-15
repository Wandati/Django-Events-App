from django import forms
from django.forms import ModelForm
from .models import Venue,Event
class EventFormAdmin(ModelForm):
    class Meta:
        model = Event
        fields = ("name","date","venue","manager","attendees","description")
        labels ={
            "name":"",
            "date":"YY:MM:DD HH:MM:SS",
            "description":"",
            "venue":"Venue",
            "manager":"Manager",
            "attendees":"Attendees"
        }
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"event name"}),
            "date":forms.TextInput(attrs={"class":"form-control","placeholder":"event date"}),
            "description":forms.Textarea(attrs={"class":"form-control","placeholder":"description"}),
            "venue":forms.Select(attrs={"class":"form-select","placeholder":"venue"}),
            "manager":forms.Select(attrs={"class":"form-select","placeholder":"manager"}),
            "attendees":forms.SelectMultiple(attrs={"class":"form-select","placeholder":"attendees"})
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ("name","date","venue","attendees","description")
        labels ={
            "name":"",
            "date":"YY:MM:DD HH:MM:SS",
            "description":"",
            "venue":"Venue",
            "attendees":"Attendees"
        }
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"event name"}),
            "date":forms.TextInput(attrs={"class":"form-control","placeholder":"event date"}),
            "description":forms.Textarea(attrs={"class":"form-control","placeholder":"description"}),
            "venue":forms.Select(attrs={"class":"form-select","placeholder":"venue"}),
            "attendees":forms.SelectMultiple(attrs={"class":"form-select","placeholder":"attendees"})
        }
        
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ("name","address","zipcode","web","email","phone","venue_img")
        labels ={
            "name":"",
            "address":"",
            "zipcode":"",
            "web":"",
            "email":"",
            "phone":"",
            "venue_img":"",
        }
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"name"}),
            "address":forms.TextInput(attrs={"class":"form-control","placeholder":"address"}),
            "zipcode":forms.TextInput(attrs={"class":"form-control","placeholder":"zipcode"}),
            "web":forms.TextInput(attrs={"class":"form-control","placeholder":"web Url"}),
            "email":forms.TextInput(attrs={"class":"form-control","placeholder":"Email Adress"}),
            "phone":forms.TextInput(attrs={"class":"form-control","placeholder":"Phone Number"})
        }
        
