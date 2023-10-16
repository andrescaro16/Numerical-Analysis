from django.shortcuts import render, redirect
from .PCM import Regla_Falsa


# Create your views here.
'''def false_rule(request):
    if request.method == 'GET':
        return render(request, 'Methods_Templates/FalseRule.html')'''

def false_rule(request):
    if request.method == 'POST':

        expresion = request.POST['latexinput']
        tol = float(request.POST['toleranciam'])
        a = float(request.POST['ai'])
        b = float(request.POST['bi'])
        k = int(request.POST['iteracionm'])
        et = request.POST['tipoe']

        tupla = Regla_Falsa.regla_falsa(expresion, a, b, et, tol, k)
        return render(request, 'Methods_Templates/FalseRule.html',
                      {'page': 'Layouts/layout_nav_bar.html', 'expresion': 'False Rule Method', 'html': tupla[0], 'mensaje_m': tupla[1]})

    if request.method == 'GET':
        return render(request,'Methods_Templates/FalseRule.html',
                              {'page': 'Layouts/layout_nav_bar.html', 'titulo': 'False Rule Method', 'alerta': 'Melo'})