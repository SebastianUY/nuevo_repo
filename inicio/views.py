from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import moto
from inicio.forms import FormularioCreacionMoto


def inicio(request):
   return render(request,'inicio.html' )

def crear_moto(request):
    
    if request.method == "POST":
        formulario = FormularioCreacionMoto(request.POST)
        if formulario.is_valid():
            marca_nueva = formulario.cleaned_data.get('marca')
            modelo_nuevo = formulario.cleaned_data.get('modelo')
            
            moto = moto(marca= marca_nueva, modelo = modelo_nuevo)
            moto.save()
    
    else:
        formulario= FormularioCreacionMoto()

    return render(request, 'inicio/crear_moto.html', {'formulario': formulario })

def listado_moto(request):
    
    moto = moto.objects.all
    
    return render(request, 'inicio'/listado_moto.html, {'listado_de_moto': moto})

    #return HttpResponse('<h1>HOLA ESTA ES MI PRIMERA VISTA</h1>')

# Create your views here