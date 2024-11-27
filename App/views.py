from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import productos


# Create your views here.
def App(request):
    return HttpResponse("Nuestra primera vista!")

from django.template import loader
def BienvenidaApp(request):
    template = loader.get_template('miPrimerTemplate.html')
    return HttpResponse(template.render())


def Productos(request):
    #return HttpResponse('Nuestra primera vista!')
    misProductos = productos.objects.all().values()
    template = loader.get_template('productos.html')
    context = {
        'misProductos': misProductos,
    }
    return HttpResponse(template.render(context, request))