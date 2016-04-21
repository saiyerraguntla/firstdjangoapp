# This class is a singleton that initializes the data only once
# and returns the data recorded when requested.

import urllib, json
import operator

from django.db import models
from django.shortcuts import get_object_or_404
from models import Event, Vendor
from django.utils import timezone


class DataSingleton:
    class __DataSingleton:
        vendorsbyevent = {}
        vendors = {}
        def __init__(self):
            url = "https://ginger.io/test-project/events/"
            response = urllib.urlopen(url)
            allData = json.loads(response.read())
            num_events = len(allData["data"])
            for event_index in range(1,num_events+1):
                url = "https://ginger.io/test-project/events/" + str(event_index) + "/"
                response = urllib.urlopen(url)
                eventdata = json.loads(response.read())
                e = Event(event_title=eventdata["data"]["name"], event_date=eventdata["data"]["start_time"])
                e.save()
                for vendor in eventdata["data"]["vendors_list"]: 
                    if self.vendors.has_key(vendor):
                        self.vendors[vendor]+=1
                    else:
                        self.vendors[vendor]=1

    instance = None
    def __init__(self):
        if not DataSingleton.instance:
            DataSingleton.instance = DataSingleton.__DataSingleton()
    def getEventsByDate(self):
        return Event.objects.order_by('-event_date')[::-1]
    # def getVendorsAtEvent(self):
    #     return 
    def getNumberEventsForVendor(self, vendor_name):
        return self.instance.vendors[vendor_name]
    def getVendorsByFrequency(self):
        sorted_tuples = sorted(self.instance.vendors.items(), key=lambda x:x[1], reverse=True)
        return [x[0] for x in sorted_tuples]

