from django.contrib import admin
from .models import Visita
from .forms import VisitaForm

class VisitaAdmin(admin.ModelAdmin):
    form = VisitaForm
    list_display = ('nombre', 'rut', 'estado', 'motivo', 'hora_entrada', 'hora_salida')
    search_fields = ('nombre', 'rut', 'motivo')
    list_filter = ('estado', 'hora_entrada')

admin.site.register(Visita, VisitaAdmin)