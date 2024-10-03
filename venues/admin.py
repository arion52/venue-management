from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Venue
from django.core.exceptions import ValidationError
from datetime import datetime

from django.contrib import admin
from .models import Venue

class VenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Only 'id' and 'name' are part of the Venue model
    search_fields = ('name',)
    ordering = ['name']

admin.site.register(Venue, VenueAdmin)


from .models import Event

from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'venue', 'start_time', 'duration')  # Use 'name' instead of 'title', and 'duration' instead of 'end_time'
    list_filter = ('venue',)
    ordering = ['start_time']

admin.site.register(Event, EventAdmin)


from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from .models import Venue, Event
from datetime import datetime

class VenueDashboardAdmin(admin.ModelAdmin):
    change_list_template = "admin/venue_dashboard.html"

    def changelist_view(self, request, extra_context=None):
        # Add custom context for dashboard stats
        booked_venues = Venue.objects.filter(events__start_time__gte=datetime.now()).count()  # Example stat
        available_venues = Venue.objects.exclude(events__start_time__gte=datetime.now()).count()
        upcoming_events = Event.objects.filter(start_time__gte=datetime.now()).count()

        extra_context = {
            'booked_venues': booked_venues,
            'available_venues': available_venues,
            'upcoming_events': upcoming_events
        }
        return super().changelist_view(request, extra_context=extra_context)

