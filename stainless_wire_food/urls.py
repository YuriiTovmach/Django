from django.conf.urls import url, include
from stainless_wire_food import views



urlpatterns = [
    url(r'^stainless_wire_food/$', views.stainless_wire_food, name='stainless_wire_food'),


]


