from django.shortcuts import render
from .models import services

def home(request):
    services = services.op
    return render(request,'root/index.html'  , context={"name ="})
    