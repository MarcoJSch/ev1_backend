from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Q
import datetime
from .models import Visita
from .forms import VisitaForm


def lista_visitas(request):
    busqueda = request.GET.get('q')
    if busqueda:
        visitas = Visita.objects.filter(Q(nombre__icontains=busqueda) | Q(rut__icontains=busqueda))#.order_by('-hora_entrada')
    else:
        visitas = Visita.objects.all()
    return render(request, 'visitas/lista_visitas.html', {'visitas': visitas})

def registrar_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            visita = form.save()
            return redirect('lista_visitas')
    else:
        form = VisitaForm()
    return render(request, 'visitas/registrar_visita.html', {'form': form})

def marcar_salida(request, pk):
    visita = get_object_or_404(Visita, pk=pk)
    if request.method == 'POST':
        hora_salida = request.POST.get('hora_salida')
        if hora_salida:
            visita.hora_salida = datetime.datetime.strptime(hora_salida, '%Y-%m-%dT%H:%M')
        else:
            visita.hora_salida = timezone.now()
        visita.estado = False
        visita.save()
        return redirect('lista_visitas')
    return render(request, 'visitas/salida.html', {'visita': visita})
