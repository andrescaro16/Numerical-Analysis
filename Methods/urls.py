from django.urls import path
from .views import *

urlpatterns = [
    #Home de la aplicación donde se seleccionaran los metodos
    path('', home_view, name='Home'),


    ##------ urlpatterns for chapter 2 ------##

    #Url para la vista de regla falsa
    path('regla_falsa/', false_rule, name='Regla Falsa'),
    #Url para el metodo grafico
    path('gragp/', graph, name='Grafica'),
    #Url para metodo de busqueda incremental
    path('incrementalSearch/', incremental_search, name='incremental_search'),
    #Url para metodo de busqueda incremental
    path('newtonRapshon/', newton_rapshon, name='newton_rapshon'),
    #Url para el metodo de raices multiples
    path('raices_multiples/', multiple_roots, name='Raices Multiples'),
    #Url para el metodo de punto fijo
    path('punto_fijo/', fixed_point, name='Punto Fijo'),
    #Url para el metodo de la secante
    path('Secante/', secante, name='Secante'),
    #Url para el metodo de la biseccion
    path('Biseccion/', biseccion, name='Biseccion'),


    ##--- urlpatterns for chapter  ---##
    
    #Url para el metodo de doolitle
    path('doolitle/', doolittle, name='process_matrix'),
    #Url para el metodo de Choleski
    path('choleski/', choleski, name='choleski_matrix'),
    #Url para el metodo de crout
    path('crout/', crout, name='crout_matrix')
]