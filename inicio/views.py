from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import moto
from inicio.forms import FormularioCreacionMoto


def inicio(request):
   return render(request,'inicio.html' )

def crear_moto(request):
    mensaje_exito = "" 
    formulario = FormularioCreacionMoto()

    if request.method == "POST":
        formulario = FormularioCreacionMoto(request.POST)
        if formulario.is_valid():
            marca_nueva = formulario.cleaned_data.get('marca')
            modelo_nuevo = formulario.cleaned_data.get('modelo')
            
            moto_nueva = moto(marca= marca_nueva, modelo = modelo_nuevo)
            moto_nueva.save()
            mensaje_exito = "¡Has ingresado una nueva moto! Muchas gracias por tu aporte."
    
  
        formulario= FormularioCreacionMoto()

    return render(request, 'crear_moto.html', {'formulario': formulario, 'mensaje_exito': mensaje_exito})


def listado_moto(request):
    
    motos = moto.objects.all()
    
    return render(request, 'listado_moto.html', {'listado_moto': motos})