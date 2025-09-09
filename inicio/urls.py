from django.urls import path
from inicio.views import inicio, crear_moto, listado_moto

urlpatterns = [
    path('', inicio, name='inicio'),
    path('moto/crear/', crear_moto, name='crear_moto'),
    path('Listado de motos/', listado_moto, name='listado_moto'),
]
