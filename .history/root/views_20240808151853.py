from django.shortcuts import render
from .models import services

def home(request):
    
    return render(request,'root/index.html' )
    