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
