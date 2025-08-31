from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
   return render(request,'inicio.html' )
    
    #return HttpResponse('<h1>HOLA ESTA ES MI PRIMERA VISTA</h1>')

# Create your views here.
