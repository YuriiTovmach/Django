from django.views.generic import ListView, DetailView
from blog.models import *
from django.shortcuts import render





def stainless_wire_food(request):
    return render(request, 'stainless_wire_food/stainless_wire_food.html', locals())








