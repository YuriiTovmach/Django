from django.conf.urls import url, include
from titanium_wire import views



urlpatterns = [
    url(r'^titanium_wire/$', views.titanium_wire, name='titanium_wire'),


]


