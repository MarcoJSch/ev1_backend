from django.urls import path
from .views import lista_visitas, registrar_visita, marcar_salida

urlpatterns = [
    path('', lista_visitas, name='lista_visitas'),
    path('registrar/', registrar_visita, name='registrar_visita'),
    path('marcar_salida/<int:pk>/', marcar_salida, name='marcar_salida'),
]