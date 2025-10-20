from django.contrib import admin
from .models import Visita
from .forms import VisitaForm

@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    form = VisitaForm
    list_display = ('nombre', 'rut', 'estado', 'motivo', 'hora_entrada', 'hora_salida')
    search_fields = ('nombre', 'rut', 'motivo')
    list_filter = ('estado', 'hora_entrada')
    list_editable = (
        'estado',
      # 'motivo',
        'hora_salida',
    )

    fieldsets = (
        ('Información Personal',{
            'fields': ('nombre', 'rut')
        }),
        ('Información de la Visita',{
            'fields': ('estado', 'motivo')
        }),
        ('Horarios',{
            'fields': ('hora_entrada', 'hora_salida'),
            'classes': ('collapse',)
        })
    )