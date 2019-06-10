from django.conf.urls import url, include
from bronze_wire import views



urlpatterns = [
    url(r'^bronze_wire/$', views.bronze_wire, name='bronze_wire'),


]


