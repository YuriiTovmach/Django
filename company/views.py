from django.shortcuts import render
# from .forms import SubscriberForm
# from products.models import *




def company(request):
    return render(request, 'company/company.html', locals())









