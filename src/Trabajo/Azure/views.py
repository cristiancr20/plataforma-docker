from django.shortcuts import render

# Create your views here.
from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.

def pasajero_view(request):
    data = { 
        'form':PasajeroForm()
    }

    if request.method == 'POST':
        formulario = PasajeroForm(data=request.POST,files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Información guardada"
        else:
            data["form"] = formulario
    return render(request, 'pasajero.html',data)

"""
def pasajero_view(request):
    form = PasajeroForm()
    if request.method == 'POST':
        form = PasajeroForm(request.POST)
        if form.is_valid():
            form.save()
    context ={
        'form':form
    }
    return render(request, "pasajero.html", context)
"""


def simulador_view(request):
    form = SimuladorForm()
    if request.method == 'POST':
        form = SimuladorForm(request.POST)
        if form.is_valid():

            form.save()
            form.cleaned_data()

    context ={
        'form':form
    }
    return render(request, "simulador.html", context)


def tarjeta_view(request):
    form = TarjetaForm()
    if request.method == 'POST':
        form = TarjetaForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data()
    context ={
        'form':form
    }
    return render(request, "tarjeta.html", context)


def bus_view(request):
    form = BusForm()
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data()
    context ={
        'form':form
    }
    return render(request, "bus.html", context)


def viaje_view(request):
    form = ViajeForm()
    if request.method == 'POST':
        form = ViajeForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data()
    context ={
        'form':form
    }
    return render(request, "viaje.html", context)