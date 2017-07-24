from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = {
    url(r'^venuelists/$', views.venue_list, name="venuelists"),
    url(r'^venuelists/(?P<pk>[0-9]+)/$', views.venue_detail, name="venuedetails"),

}

urlpatterns = format_suffix_patterns(urlpatterns)