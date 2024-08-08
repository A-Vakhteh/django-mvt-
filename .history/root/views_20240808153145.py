from django.shortcuts import render
from .models import services

def home(request):
    services = services.objects.
    return render(request,'root/index.html'  , context={"name ="})
    