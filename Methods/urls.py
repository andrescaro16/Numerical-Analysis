from django.urls import path
from .views import *

urlpatterns = [
    path('', false_rule, name='Regla Falsa')
]