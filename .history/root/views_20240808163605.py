from django.shortcuts import render
from .models import services

def home(request):
    #service = services.objects.all()
    service = services.objects.f
    return render(request,'root/index.html' , context={"name": service})
    