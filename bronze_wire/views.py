from django.views.generic import ListView, DetailView
from blog.models import *
from django.shortcuts import render





def bronze_wire(request):
    return render(request, 'bronze_wire/bronze_wire.html', locals())








