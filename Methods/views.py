from django.shortcuts import render, redirect
from .PCM import Regla_Falsa, Busqueda_incremental, Newton_rapshon


# Create your views here.
'''def false_rule(request):
    if request.method == 'GET':
        return render(request, 'Methods_Templates/FalseRule.html')'''

def false_rule(request):
    if request.method == 'GET':
        return render(request,'Methods_Templates/FalseRule.html',
                      {'page': 'Layouts/layout_nav_bar.html', 'titulo': 'False Rule Method', 'alerta': 'Melo'})

    if request.method == 'POST' and 'latexinput' in request.POST:
        try:
            expresion = request.POST['latexinput']
            tol = float(request.POST['toleranciam'])
            a = float(request.POST['ai'])
            b = float(request.POST['bi'])
            k = int(request.POST['iteracionm'])
            et = request.POST['tipoe']

            tupla = Regla_Falsa.regla_falsa(expresion, a, b, et, tol, k)
            return render(request, 'Methods_Templates/FalseRule.html',
                          {'page': 'Layouts/layout_nav_bar.html', 'expresion': 'False Rule Method', 'html': tupla[0], 'mensaje_m': tupla[1]})
        except ValueError as e:
            return render(request, 'Methods_Templates/FalseRule.html',
                          {'page': 'Layouts/layout_nav_bar.html', 'mensaje': e, 'alerta': 'Fallo'})
    else:
        return render(request, 'Methods_Templates/FalseRule.html',
                      {'page': 'Layouts/layout_nav_bar.html', 'titulo': 'False Rule Method', 'alerta': 'Melo'})

def incremental_search(request):
    if request.method == 'GET':
        return render(request, 'Methods_Templates/incrementalSearch.html',
                      {'page': 'Layouts/layout_nav_bar.html', 'titulo': 'Incremental Search Method', 'alerta': 'Melo'})
    if request.method == 'POST' and 'latexinput' in request.POST:
        try:
            expresion = request.POST['latexinput']
            tol = float(request.POST['toleranciam'])
            a = float(request.POST['ai'])
            b = float(request.POST['bi'])
            k = int(request.POST['iteracionm'])
            #et = request.POST['tipoe']

            tupla = Busqueda_incremental.busqueda_incremental(expresion, a, b, tol, k)
            return render(request, 'Methods_Templates/incrementalSearch.html',
                          {'page': 'Layouts/layout_nav_bar.html', 'expresion': 'Incremental Search Method', 'html': tupla[0], 'mensaje_m': tupla[1]})
        except ValueError as e:
            return render(request, 'Methods_Templates/incrementalSearch.html',
                          {'page': 'Layouts/layout_nav_bar.html', 'mensaje': e, 'alerta': 'Fallo'})
    else:
        return render(request, 'Methods_Templates/incrementalSearch.html',
                      {'page': 'Layouts/layout_nav_bar.html', 'titulo': 'Incremental Search Method', 'alerta': 'Melo'})

def newton_rapshon(request):
    if request.method == 'GET':
        return render(request, 'Methods_Templates/newtonRapshon.html',
                      {'page': 'Layouts/layout_nav_bar.html', 'titulo': 'Incremental Search Method', 'alerta': 'Melo'})
    if request.method == 'POST' and 'latexinput' in request.POST:
        try:
            expresion = request.POST['latexinput']
            tol = float(request.POST['toleranciam'])
            a = float(request.POST['ai'])
            k = int(request.POST['iteracionm'])
            et = request.POST['tipoe']

            tupla = Newton_rapshon.newton_rapshon(expresion, a, tol, k, et)
            return render(request, 'Methods_Templates/newtonRapshon.html',
                          {'page': 'Layouts/layout_nav_bar.html', 'expresion': 'newton Rapshon Method', 'html': tupla[0], 'mensaje_m': tupla[1]})
        except ValueError as e:
            return render(request, 'Methods_Templates/newtonRapshon.html',
                          {'page': 'Layouts/layout_nav_bar.html', 'mensaje': e, 'alerta': 'Fallo'})
    else:
        return render(request, 'Methods_Templates/newtonRapshon.html',
                      {'page': 'Layouts/layout_nav_bar.html', 'titulo': 'newton Rapshon Method', 'alerta': 'Melo'})

def home_view(request):
    if request.method == 'GET':
        return render(request,'Methods_Templates/Home.html',
                              {'page': 'Layouts/layout_nav_bar.html', 'titulo': 'Home', 'alerta': 'Melo'})

def graph(request):
    if request.method == 'GET':
        return render(request,'Methods_Templates/Graph.html',
                              {'titulo': 'Grafica', 'alerta': 'Melo'})
    if request.method == 'POST':
        return render(request, 'Methods_Templates/Graph.html',
                      {'titulo': 'Grafica', 'alerta': 'Melo'})