
from django.contrib import admin
from .models import *



class AdminViaje (admin.ModelAdmin):
    list_display = ["__str__","pasajero","bus","costo","cantidad","fecha_viaje","efectivo"]
    class Meta(object):
        model=Viaje


class AdminSimulador(admin.ModelAdmin):
    list_display = ["__str__","numero","fecha_viaje","viaje","tarjeta"]
    class Meta(object):
        model=SimularAccesoPago

class AdminTarjeta(admin.ModelAdmin):
    list_display = ["__str__","codigo","monto","idPasajero"]
    class Meta(object):
        model=Tarjeta

class AdminPasajero (admin.ModelAdmin):
    list_display = ["__str__","cedula","nombre","apellido","email","edad","sexo"]
    class Meta(object):
        model=Pasajero
        
admin.site.register(Bus)
admin.site.register(Viaje,AdminViaje)    
admin.site.register(SimularAccesoPago, AdminSimulador)    
admin.site.register(Tarjeta, AdminTarjeta)
admin.site.register(Pasajero, AdminPasajero)