from django.views.generic import ListView, DetailView
from blog.models import *
from django.shortcuts import render





def stainless_wire_technical(request):
    return render(request, 'stainless_wire_technical/stainless_wire_technical.html', locals())








