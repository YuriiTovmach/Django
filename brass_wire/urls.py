from django.conf.urls import url, include
from brass_wire import views



urlpatterns = [
    url(r'^brass_wire/$', views.brass_wire, name='brass_wire'),


]


