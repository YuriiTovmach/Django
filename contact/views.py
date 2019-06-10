from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *



def contact(request):
    name = "Yurii"
    current_day = "20.05.2019"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(request, 'landing/contact.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_ok = products_images.filter(product__category__id=1)
    products_images_knitting = products_images.filter(product__category__id=2)
    products_images_welding = products_images.filter(product__category__id=3)
    products_images_nichrome = products_images.filter(product__category__id=4)
    products_images_galvanized = products_images.filter(product__category__id=5)
    products_images_spring = products_images.filter(product__category__id=6)
    return render(request, 'landing/home.html', locals())









