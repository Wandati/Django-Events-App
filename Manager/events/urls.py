from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("<int:year>/<str:month>/",views.index,name="home"),
    path("events/",views.list_events,name="events"),
    path("venues/",views.list_venues,name="venues"),
    # path("venues_text/",views.venues_text,name="venues_text"),
    path("venues_csv/",views.venues_csv,name="venues_csv"),
    path("venues_pdf/",views.venues_pdf,name="venues_pdf"),
    path("add_venue/",views.add_venue,name="add_venue"),
    path("add_event/",views.add_event,name="add_event"),
    path("my_events/",views.my_events,name="my_events"),
    path("searched_venues/",views.searched_venues,name="searched_venues"),
    path("venue_data/<int:venue_id>",views.venue_data,name="venue_data"),
    path("update_venue/<int:venue_id>",views.update_venue,name="update_venue"),
    path("update_event/<int:event_id>",views.update_event,name="update_event"),
    path("delete_event/<int:event_id>",views.delete_event,name="delete_event"),
    path("delete_venue/<int:venue_id>",views.delete_venue,name="delete_venue"),
    path("admin_approval/",views.admin_approval,name="admin_approval"),
    path('venue_events/<venue_id>', views.venue_events, name='venue-events'),
	path('show_event/<event_id>', views.show_event, name='show-event'),
    # path('show_venue/<venue_id>', views.show_venue, name='show-venue'),

]
