import json
from pathlib import Path
from django.http import HttpResponse
from django.shortcuts import render
from .models import PrecioServicio, Servicio


def cargar_datos():
    archivo = Path(__file__).resolve().parent / "datos.json"
    with open(archivo, "r", encoding="utf-8") as archivo_json:
        return json.load(archivo_json)

def servicios(request):
    datos = cargar_datos()
    return render(request, 'serviciosApp/servicios.html', {'servicios': datos})

def precios(request):
    datos = cargar_datos()
    return render(request, 'serviciosApp/precios.html', {'servicios': datos})

def servicios_old(request):
    datos = cargar_datos()
    pagina = "<h1>Nuestros Servicios</h1>"
    for servicio in datos:
        pagina += f""" 
            <h2>{servicio['nombre']}</h2>
            <p><strong>ID:</strong> {servicio['id']}</p>
            <p><strong>Descripción:</strong> {servicio['descripcion']}</p>
            <p><strong>Precio:</strong> ${servicio['precio']}</p>
            <p><strong>Disponibilidad:</strong> {servicio['disponibilidad']}</p>
            <hr>
        """
    pagina += '<br><a href="/">Volver al menú principal</a>'
    return HttpResponse(pagina)


"""def precios(request):
    pagina = '''
    <h1>Precios</h1>
    <ul>
        <li>Servicio 1: $150.000</li>
        <li>Servicio 2: $250.000</li>
        <li>Servicio 3: $100.000</li>
    </ul>
    <a href="/">Volver al menú</a>
    '''

    return HttpResponse(pagina)"""