from django.conf.urls import url, include
from copper_wire import views



urlpatterns = [
    url(r'^copper_wire/$', views.copper_wire, name='copper_wire'),


]


