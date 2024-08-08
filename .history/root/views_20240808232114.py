from django.shortcuts import render
from .models import *

def home(request):
    #service = services.objects.all()
    service = services.objects.filter(status=True)
    return render(request,'root/index.html' , context={"name": service})

def trainers(request):
    #service = services.objects.all()
    train = trainer.objects.all()
    return render(request,'root/index.html' , context={"tr": train})

def question(request):
    
    train = trainer.objects.all()
    return render(request,'root/index.html' , context={"qu": train})


   
    