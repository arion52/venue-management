from django.urls import path
from .views import VenueList, VenueBooking
from . import views

urlpatterns = [
    path('venues/', VenueList.as_view(), name='venue-list'),
    path('venues/<int:pk>/book/', VenueBooking.as_view(), name='venue-booking'),  # Booking URL
    path('events/', views.event_list, name='event_list'),  # List all events
    path('events/<int:id>/', views.event_detail, name='event_detail'),  # Get event details by event ID
]