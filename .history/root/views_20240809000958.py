from django.shortcuts import render
from .models import *

def home(request):
    #service = services.objects.all()
    service = services.objects.filter(status=True)
    que = question.objects.all()
    train = trainer.objects.all()
    context = {
        'tr' : train,
        'q'
        
    }
    
    return render(request,'root/index.html' , context={"name": service})




   
    