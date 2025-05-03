from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):  
     months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']  
     
     return render(request, 'myapp/months.html', {'months': months})

