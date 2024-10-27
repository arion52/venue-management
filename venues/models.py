from datetime import timedelta
from django.db import models
from pydantic import ValidationError

class Venue(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_booked = models.BooleanField(default=False)
    booked_by = models.CharField(max_length=255, blank=True, null=True)
    booked_at = models.DateTimeField(blank=True, null=True)
    booking_duration = models.IntegerField(blank=True, null=True)  # Duration in hours

    def __str__(self):
        return self.name

from datetime import timedelta

from datetime import timedelta
from django.db import models

class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    duration = models.IntegerField()  # Duration in hours
    end_time = models.DateTimeField()  # End time will be auto-calculated

    def save(self, *args, **kwargs):
        # Automatically calculate end_time based on start_time and duration
        self.end_time = self.start_time + timedelta(hours=self.duration)
        super().save(*args, **kwargs)
