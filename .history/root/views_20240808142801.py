from django.shortcuts import render
بقخئ

def home(request):
    return render(request,'root/index.html')
    