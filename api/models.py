from datetime import datetime

from django.db import models

# Create your models here.
class VenueList(models.Model):
    venue_name = models.CharField(max_length=255, blank=False)
    venue_url = models.CharField(max_length=255, blank=False)
    venue_address = models.CharField(max_length=255, blank=False)
    venue_lat_long = models.CharField(max_length=255, blank=False)
    venue_contact = models.TextField(max_length=255, blank=False)
    venue_details = models.TextField(max_length=255, blank=False)
    venue_city = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{}".format(self.venue_name)

class EventList(models.Model):
    venue = models.ForeignKey(VenueList, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255, blank=False)
    event_price = models.DecimalField(max_digits=6, decimal_places=2)
    event_detail = models.TextField(max_length=255, blank=False)
    #time_start_end = models.CharField(max_length=255, blank=False)
    event_time_start = models.TimeField(blank=False, null=False)
    event_time_end = models.TimeField(blank=False, null=False)
    event_url = models.CharField(max_length=255, blank=False)
    event_img_url = models.CharField(max_length=255, blank=False)
    event_date_time = models.DateField(blank=False, editable=True)

    def __str__(self):
        return "{}".format(self.event_name)
