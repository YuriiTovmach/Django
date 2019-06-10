from django.views.generic import ListView, DetailView
from blog.models import *
from django.shortcuts import render





def copper_wire(request):
    return render(request, 'copper_wire/copper_wire.html', locals())








