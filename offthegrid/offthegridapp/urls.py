from django.conf.urls import url

from . import views

app_name = 'offthegrid'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events/$', views.events, name='events'),
    url(r'^vendors/$', views.vendors, name='vendors'),
    url(r'^(?P<event_id>[0-9]+)/$', views.display_event, name='display_event'),
    url(r'^(?P<event_id>[0-9]+)/vendors/$', views.display_vendors_at_event, name='display_vendors_at_event'),
    url(r'^vendor/(?P<vendor_name>(.*)+)/$', views.display_vendor_page, name='display_vendor_page'),
]