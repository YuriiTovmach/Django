from django.contrib import admin
from .models import *

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass
