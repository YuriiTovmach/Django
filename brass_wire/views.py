from django.views.generic import ListView, DetailView
from blog.models import *
from django.shortcuts import render





def brass_wire(request):
    return render(request, 'brass_wire/brass_wire.html', locals())








