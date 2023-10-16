from django.urls import path
from .views import *

urlpatterns = [
    #Home de la aplicación donde se seleccionaran los metodos
    path('', home_view, name='Home'),
    #Url para la vista de regla falsa
    path('regla_falsa/', false_rule, name='Regla Falsa'),
    #Url para el metodo grafico
    path('gragp/', graph, name='Grafica')
]