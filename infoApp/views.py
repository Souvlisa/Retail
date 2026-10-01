from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def informacion(request):
    return render(request, 'infoApp/index.html')

"""def informacion(request):
    titulo = "<h1>Quienes Somos</h1>"
    info = "<p>Aquí va información relevante.</p>"
    volver = "<br><a href='../'>Volver</a>"
    pagina = titulo + info + volver
    return HttpResponse(pagina)"""