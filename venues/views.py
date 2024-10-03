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
        venue = self.get_object()

        # Check if the venue is already booked
        if venue.is_booked:
            return JsonResponse({'error': 'Venue is already booked'}, status=status.HTTP_400_BAD_REQUEST)

        # Get booking details from request
        booked_by = request.data.get('booked_by')
        booked_at = request.data.get('booked_at')
        booking_duration = request.data.get('booking_duration')
        event_name = request.data.get('event_name')
        event_description = request.data.get('event_description')
        start_time = request.data.get('start_time')

        # Check if all required fields are provided
        if not all([booked_by, booked_at, booking_duration, event_name, event_description, start_time]):
            return JsonResponse({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Calculate end time from start time and duration
        end_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S') + timedelta(hours=booking_duration)

        # Check if the venue is available for the specified time
        if not is_venue_available(venue, datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S'), end_time):
            return JsonResponse({'error': 'Venue is not available for the selected time'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new event
        event = Event(
            venue=venue,
            name=event_name,
            description=event_description,
            start_time=datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S'),
            duration=booking_duration
        )
        event.save()

        # Update venue booking status
        venue.is_booked = True
        venue.booked_by = booked_by
        venue.booked_at = booked_at
        venue.booking_duration = booking_duration
        venue.save()

        return JsonResponse({'success': 'Venue booked successfully for event'}, status=status.HTTP_200_OK)
class VenueBooking(generics.UpdateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

    def patch(self, request, *args, **kwargs):
        venue = self.get_object()

        # Check if the venue is already booked
        if venue.is_booked:
            return JsonResponse({'error': 'Venue is already booked'}, status=status.HTTP_400_BAD_REQUEST)

        # Get booking details from request
        booked_by = request.data.get('booked_by')
        booked_at = request.data.get('booked_at')
        booking_duration = request.data.get('booking_duration')
        event_name = request.data.get('event_name')
        event_description = request.data.get('event_description')
        start_time = request.data.get('start_time')

        # Check if all required fields are provided
        if not all([booked_by, booked_at, booking_duration, event_name, event_description, start_time]):
            return JsonResponse({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Calculate end time from start time and duration
        end_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S') + timedelta(hours=booking_duration)

        # Check if the venue is available for the specified time
        if not is_venue_available(venue, datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S'), end_time):
            return JsonResponse({'error': 'Venue is not available for the selected time'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new event
        event = Event(
            venue=venue,
            name=event_name,
            description=event_description,
            start_time=datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S'),
            duration=booking_duration
        )
        event.save()

        # Update venue booking status
        venue.is_booked = True
        venue.booked_by = booked_by
        venue.booked_at = booked_at
        venue.booking_duration = booking_duration
        venue.save()

        return JsonResponse({'success': 'Venue booked successfully for event'}, status=status.HTTP_200_OK)


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
