from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Venue
from .serializers import VenueSerializer
from django.http import JsonResponse

# To list all venues and their booking status
class VenueList(generics.ListAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

# admin user: jaz
# admin pwd: baru2005

# To book a venue
from rest_framework import generics
from .models import Venue, Event
from .serializers import VenueSerializer, EventSerializer  # Make sure to create an EventSerializer
from django.http import JsonResponse
from rest_framework import status

# To book a venue for a new event
class VenueBooking(generics.UpdateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

    def patch(self, request, *args, **kwargs):
        print(request.data)
        venue = self.get_object()

        if venue.is_booked:
            return JsonResponse({'error': 'Venue is already booked'}, status=status.HTTP_400_BAD_REQUEST)

        # Extract and validate all fields
        required_fields = ['booked_by', 'booked_at', 'booking_duration', 'event_name', 'event_description', 'start_time']
        for field in required_fields:
            if not request.data.get(field):
                return JsonResponse({'error': f'Missing field: {field}'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Parse incoming data
            booked_by = request.data['booked_by']
            booked_at = request.data['booked_at']
            booking_duration = int(request.data['booking_duration'])
            event_name = request.data['event_name']
            event_description = request.data['event_description']
            start_time = request.data['start_time']

            # Convert start_time to a Python datetime object
            start_time_obj = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S')
            end_time = start_time_obj + timedelta(hours=booking_duration)

            # Log venue availability check details
            print(f"Checking venue availability: Start Time - {start_time_obj}, End Time - {end_time}")
            if not is_venue_available(venue, start_time_obj, end_time):
                return JsonResponse({'error': 'Venue is not available for the selected time'}, status=status.HTTP_400_BAD_REQUEST)

            # Create the event and update the venue
            event = Event(
                venue=venue,
                name=event_name,
                description=event_description,
                start_time=start_time_obj,
                duration=booking_duration
            )
            event.save()

            venue.is_booked = True
            venue.booked_by = booked_by
            venue.booked_at = booked_at
            venue.booking_duration = booking_duration
            venue.save()

            return JsonResponse({'success': 'Venue booked successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


from datetime import datetime

def is_venue_available(venue, start_time, end_time):
    conflicting_events = venue.events.filter(
        start_time__lt=end_time, end_time__gt=start_time
    )
    return not conflicting_events.exists()

from django.http import JsonResponse
from .models import Event
from django.shortcuts import get_object_or_404
from datetime import timedelta

# List all events
def event_list(request):
    events = Event.objects.all()
    data = []
    for event in events:
        data.append({
            'id': event.id,
            'name': event.name,
            'description': event.description,
            'venue': event.venue.name,
            'start_time': event.start_time,
            'duration': event.duration,
            'end_time': event.start_time + timedelta(hours=event.duration)
        })
    return JsonResponse(data, safe=False)

# Get event details by event ID
def event_detail(request, id):
    event = get_object_or_404(Event, pk=id)
    data = {
        'id': event.id,
        'name': event.name,
        'description': event.description,
        'venue': event.venue.name,
        'start_time': event.start_time,
        'duration': event.duration,
        'end_time': event.start_time + timedelta(hours=event.duration)
    }
    return JsonResponse(data)
