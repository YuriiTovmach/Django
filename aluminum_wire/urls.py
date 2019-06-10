from django.conf.urls import url, include
from aluminum_wire import views



urlpatterns = [
    url(r'^aluminum_wire/$', views.aluminum_wire, name='aluminum_wire'),


]


