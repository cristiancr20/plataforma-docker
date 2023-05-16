from statistics import mode
from tabnanny import verbose
from django.db import models
from django.forms import IntegerField
from .choices import *
# Create your models here.

class Pasajero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)
    email = models.EmailField(verbose_name='Correo')
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=9,verbose_name='Genero',choices=sexos, default='F')
    
    def __str__(self) :
        return '{}'.format(self.nombre)
    

        
class Tarjeta(models.Model):
    monto = models.CharField(max_length=3, blank=False)
    codigo= models.CharField(max_length=6, blank=False)
    idPasajero =models.ForeignKey(Pasajero, on_delete=models.CASCADE)

    def __str__(self):
        return f'Tarjeta: {self.codigo} | Pasajero: {str(self.idPasajero)} | Monto Tarjeta: {str(self.monto)}'



class Bus(models.Model):
    placa = models.CharField(max_length=7 , blank=False)
    capacidad = models.CharField(max_length=2 , blank=False)
    numerobus= models.CharField(max_length=2 , blank=False)
    tipo = models.CharField(max_length=7,verbose_name='Tipo',choices=tipo, default='F')

    idTarjeta= models.ManyToManyField(Pasajero, through='Viaje')
    
    def __str__(self) :
        return '{}'.format(self.placa)


class Viaje(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    costo = models.DecimalField(max_digits=4, decimal_places=2)
    cantidad = models.IntegerField()
    fecha_viaje= models.DateTimeField(auto_now_add=True)
    efectivo= models.BooleanField(default=True)
    
    def __str__(self):
       return f'Pasajero: {self.pasajero.cedula} | Nombre: {str(self.pasajero.nombre)} | Precio: {str(self.costo)}'


class SimularAccesoPago(models.Model):
    numero= models.CharField(max_length=7, blank=False)
    fecha_viaje= models.DateTimeField(auto_now_add=True)
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    tarjeta =  models.ForeignKey(Tarjeta, on_delete=models.CASCADE)


    def __str__(self) :
        return f'Pasajero:  {str(self.viaje.pasajero.nombre)}'
