from django.contrib import admin
from .models import EventUser,Venue,Event
from django.contrib.auth.models import Group
# Register your models here.

admin.site.register(EventUser)
# admin.site.register(Venue)
# admin.site.register(Event)
admin.site.unregister(Group)
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display=("name","address","phone")
    ordering=("name",)
    search_fields=("name","address")
    
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields=("name","venue","manager","date","attendees","is_approved")
    list_filter=("venue","date")
    ordering=("-date",)
    list_display=("name","venue","date","is_approved")