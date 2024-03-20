from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact
# Create your views here.
def index(request):
    context={
        'variable1':'hello baby',
        'variable2':'i am fine',
    }
    return render(request , 'index.html', context)

def about(request):
   return render(request , 'about.html', )

def services(request):
    return render(request , 'services.html', )

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        
        contact=Contact(name=name , email=email , phone=phone )
        contact.save()   
    return render(request,'contact.html')
