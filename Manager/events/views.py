from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from .models import Event,Venue
from .forms import VenueForm,EventForm,EventFormAdmin
from django.http import HttpResponseRedirect,HttpResponse,FileResponse
import csv
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
from datetime import datetime
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

def index(request,year=datetime.utcnow().year,month=datetime.utcnow().strftime("%B")):
    month = month.capitalize()
    month_date = int(list(calendar.month_name).index(month))
    cal = HTMLCalendar().formatmonth(year,month_date)
    time = datetime.utcnow().strftime("%H:%M %P")
    events = Event.objects.filter(
        date__year=year,
        date__month=month_date
    )
    return render(request,"events/index.html",{"cal":cal,"month":month,"year":year,"time":time,"events":events})

def venues_pdf(request):
    # Create Bytestream buffer
	buf = io.BytesIO()
	# Create a canvas
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	# Create a text object
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica", 14)

	# Designate The Model
	venues = Venue.objects.all()

	# Create blank list
	lines = []

	for venue in venues:
		lines.append(venue.name)
		lines.append(venue.address)
		lines.append(venue.zipcode)
		lines.append(venue.phone)
		lines.append(venue.web)
		lines.append(venue.email)
		lines.append(" ")

	# Loop
	for line in lines:
		textob.textLine(line)

	# Finish Up
	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	# Return something
	return FileResponse(buf, as_attachment=True, filename='venue.pdf')


def venues_csv(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Dispostion']='attachment; filename=text.csv'
    writer=csv.writer(response)
    writer.writerow(['Venue Name','Address','Zip Code','Email','Web Url','Email'])
    venues = Venue.objects.all()
    for venue in venues:
        writer.writerow([venue.name,venue.address,venue.zipcode,venue.email,venue.web,venue.email])
    return response
# def venues_text(request):
#     response = HttpResponse(content_type='application/octet-stream')
#     response['Content_Disposition']='attachment; filename=venues.txt'
#     venues = Venue.objects.all()
#     # lines=[]
#     # for venue in venues:
#     #     lines.append(venue)
#     # response.writelines(lines)
#     # return response
#     lines=[
#         {'name':venue.name,
#          'address':venue.address,
#          'zipcode':venue.zipcode,
#          'email':venue.email,
#          'web':venue.web,
#          'phone':venue.phone
#         }
#         for venue in venues
#     ]
#     response.writelines(lines)
#     return response
def list_events(request):
    if request.method == "POST":
        searched=request.POST["search"]
        events = Event.objects.filter(name__contains=searched)
    else:
        events = Event.objects.all().order_by("-date")
    return render(request,"events/events_list.html",{"events":events})

def my_events(request):
    events = Event.objects.filter(attendees=request.user.id)
    return render(request,"events/my_events.html",{"events":events})
def add_event(request):
    submitted = False
    
    if request.method == "POST":
        if request.user.is_superuser:
            form = EventFormAdmin(request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/add_event/?submitted=True')
        else:
            form=EventForm(request.POST)
            if form.is_valid():
                event = form.save(commit=False)
                event.manager=request.user
                event.save()
            return HttpResponseRedirect('/add_event/?submitted=True')
    else:
        if request.user.is_superuser:
            form = EventFormAdmin
        else:
            form = EventForm
        if "submitted" in request.GET:
            submitted=True
    return render(request,"events/add_event.html",{"submitted":submitted,"form":form})
def update_event(request,event_id):
    event = Event.objects.get(pk=event_id)
    if request.user.is_superuser:
        form = EventFormAdmin(request.POST or None,instance=event)
    else:
        form = EventForm(request.POST or None,instance=event)
    if form.is_valid():
        form.save()
        return redirect('events')
    return render(request,"events/update_event.html",{"form":form,"event":event})
def delete_event(request,event_id):
    event=Event.objects.get(pk=event_id)
    if request.user == event.manager:
        event.delete()
        messages.success(request,"Event Deleted Successfully!!!")
        return redirect("events")
    else:
        messages.error(request,"Unauthorized.Cannot delete this Event!")
        return redirect("events")
def add_venue(request):
    submitted=False
    if request.user.is_superuser:
        if request.method == "POST":
            form = VenueForm(request.POST,request.FILES)
            if form.is_valid():
                venue=form.save(commit=False)
                venue.owner = request.user.id
                venue.save()
                return HttpResponseRedirect("/add_venue/?submitted=True")
        else:
            form =VenueForm
            if "submitted" in request.GET:
                submitted = True
    else:
        messages.error(request,"Unauthorized")
        return redirect("venues")    
    return render(request,"events/add_venue.html",{"form":form,"submitted":submitted})
 
def list_venues(request):
    # venues = Venue.objects.all().order_by("name")
    venues_list = Venue.objects.all()
    p = Paginator(venues_list,2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = 'a' * venues.paginator.num_pages
    return render(request,"events/venues.html",{"venues":venues,"venues_list":venues_list,"nums":nums})

def venue_data(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    owner = User.objects.get(pk=venue.owner)
    return render(request,"events/venue_data.html",{"venue":venue,"owner":owner})

def searched_venues(request):
    if request.method == "POST":
        searched = request.POST['searched_venues']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request,"events/search_venues.html",{"venues":venues})
    return render(request,"events/search_venues.html")

def update_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    if request.user.is_superuser:
        form = VenueForm(request.POST or None,request.FILES or None,instance=venue)
        if form.is_valid():
            form.save()
            return redirect("venues")
    else:
        messages.error(request,"Unauthorized.")
        return redirect('venues')
        
    return render(request,"events/update_venue.html",{"venue":venue,"form":form})
def delete_venue(request,venue_id):
    venue=Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect("venues")

def venue_events(request, venue_id):
	venue = Venue.objects.get(id=venue_id)	
	events = venue.event_set.all()
	if events:
		return render(request, 'events/venue_events.html', {
			"events":events
			})
	else:
		messages.error(request, ("This Venue Has No Events At This Time..."))
		return redirect('home')

def show_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	return render(request, 'events/show_event.html', {
			"event":event
			})
def admin_approval(request):
    venue_list = Venue.objects.all()
    user_count=User.objects.all().count()
    event_count=Event.objects.all().count()
    venue_count=Venue.objects.all().count()
    events = Event.objects.all().order_by("-date")
    if request.user.is_superuser:
        if request.method == "POST":
            id_list = request.POST.getlist('boxes')
            events.update(is_approved=False)
            for x in id_list:
                Event.objects.filter(pk=int(x)).update(is_approved=True)
            messages.success(request, ("Event List Approval Has Been Updated!"))
            return redirect("events")
        else:
            return render(request, "events/admin.html", {"events": events,"user_count":user_count,"event_count":event_count,"venue_count":venue_count,"venue_list":venue_list})
    else:
        messages.error(request, ("You aren't authorized to view this page!"))
        return redirect('home')
