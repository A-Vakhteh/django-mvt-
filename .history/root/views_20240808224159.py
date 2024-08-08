from django.shortcuts import render
from .models import *

def home(request):
    #service = services.objects.all()
    service = services.objects.filter(status=True)
    return render(request,'root/index.html' , context={"name": service})

def trainer(request):
    #service = services.objects.all()
    service = services.objects.filter(status=True)
    return render(request,'root/index.html' , context={"name": service})

   
    