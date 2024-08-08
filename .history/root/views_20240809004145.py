from django.shortcuts import render
from .models import *

def home(request):
    #service = services.objects.all()
    service = services.objects.filter(status=True)
    que = question.objects.all()
    train = trainer.objects.all()
    sserve = s_service.objects.all()
    context = {
        'tr' : train,
        'que': que,
        'name': service,
        'ss':
    }
    
    return render(request,'root/index.html' , context=context)




   
    