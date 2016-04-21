from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from data import DataSingleton

from models import Event

def index(request):
    context = {}
    return render(request, 'offthegridapp/index.html', context)

def events(request):
    ordered_event_list = DataSingleton().getEventsByDate()
    context = {'ordered_event_list': ordered_event_list}
    return render(request, 'offthegridapp/events.html', context)

def vendors(request):
    vendors_list = DataSingleton().getVendorsByFrequency()
    context = {'vendors_list': vendors_list}
    return render(request, 'offthegridapp/display_vendors_at_event.html', context)

def display_event(request, event_id):
    response = "Here is the list of upcoming events %s:"
    return HttpResponse(response % event_id)

def display_vendors_at_event(request, event_id):
    vendors_list = DataSingleton().getVendorsByFrequency()
    context = {'vendors_list': vendors_list}
    return render(request, 'offthegridapp/display_vendors_at_event.html', context)

def display_vendor_page(request, vendor_name):
	vendor_info = [vendor_name, DataSingleton().getNumberEventsForVendor(vendor_name)]
	context = {'vendor_info': vendor_info}
	return render(request, 'offthegridapp/display_vendor_page.html', context)


