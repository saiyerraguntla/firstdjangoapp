
from django.db import models

class Event(models.Model):
    event_title = models.CharField(max_length=500)
    event_date = models.DateTimeField('Event Date')
    def date(self):
        return self.event_date
    def __str__(self):
        return self.event_title


class Vendor(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	vendor_name = models.CharField(max_length=200)
	def __str__(self):
		return self.vendor_name