from django.views.generic import ListView, DetailView
from blog.models import *
from django.shortcuts import render





def titanium_wire(request):
    return render(request, 'titanium_wire/titanium_wire.html', locals())








