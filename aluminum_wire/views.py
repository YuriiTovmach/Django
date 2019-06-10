from django.views.generic import ListView, DetailView
from blog.models import *
from django.shortcuts import render





def aluminum_wire(request):
    return render(request, 'aluminum_wire/aluminum_wire.html', locals())








