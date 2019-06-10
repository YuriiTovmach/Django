from django.shortcuts import render
from service.models import Service

def index(request):
    """ main page """

    context = {}
    services = Service.objects.all()
    context['services'] = services

    template = 'service/service.html'
    return render(request, template, context)