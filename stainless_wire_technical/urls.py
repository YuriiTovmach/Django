from django.conf.urls import url, include
from stainless_wire_technical import views



urlpatterns = [
    url(r'^stainless_wire_technical/$', views.stainless_wire_technical, name='stainless_wire_technical'),


]


