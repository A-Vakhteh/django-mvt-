from django.shortcuts import render
from .models

def home(request):
    return render(request,'root/index.html')
    