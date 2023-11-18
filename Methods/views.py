from django.http import HttpResponse
from django.shortcuts import render, redirect
from .PCM import Regla_Falsa, Busqueda_incremental, Newton_rapshon, Doolitle
from .PCM import Multiple_Roots
from .PCM import Secante
from .PCM import Biseccion
from .PCM import Choleski



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

def multiple_roots(request):
    if request.method == 'GET':
        return render(request,'Methods_Templates/Multiple_Roots.html',
                      {'titulo': 'Raices Multiples', 'alerta': 'Melo'})
    #fx, xi, tol, k, et
    if request.method == 'POST' and 'latexinput' in request.POST:
        try:
            expresion = request.POST['latexinput']
            tol = float(request.POST['toleranciam'])
            xi = float(request.POST['xi'])
            k = int(request.POST['iteracionm'])
            et = request.POST['tipoe']

            tupla = Multiple_Roots.multiple_roots(expresion, xi, tol, k, et)
            return render(request, 'Methods_Templates/Multiple_Roots.html',
                          {'page': 'Layouts/layout_nav_bar.html', 'expresion': 'Raices Multiples', 'html': tupla[0], 'mensaje_m': tupla[1]})
        except ValueError as e:
            return render(request, 'Methods_Templates/Multiple_Roots.html',
                          {'page': 'Layouts/layout_nav_bar.html', 'mensaje': e, 'alerta': 'Fallo'})
    else:
        return render(request, 'Methods_Templates/Multiple_Roots.html',
                      {'page': 'Layouts/layout_nav_bar.html', 'titulo': 'Raices Multiples', 'alerta': 'Melo'})
    
def secante(request):
    if request.method == 'GET':
        return render(request,'Methods_Templates/secante.html',
                      {'titulo': 'secante', 'alerta': 'Melo'})
    #Valores de entrada: Fx, x0, xi, tol, niter
    if request.method == 'POST' and 'latexinput' in request.POST:
        try:
            expression = request.POST['latexinput']
            tol = float(request.POST['toleranciam'])
            x0 = float(request.POST['x0'])
            xi = float(request.POST['xi'])
            k = int(request.POST['iteracionm'])
        

            tupla = Secante.secante(expression, xi, x0, tol, k)
            return render(request, 'Methods_Templates/secante.html',
                          {'page': 'Layouts/layout_nav_bar.html', 'expresion': 'Secante', 'html': tupla[0], 'mensaje_m': tupla[1]})
        except ValueError as e:
            return render(request, 'Methods_Templates/secante.html',
                          {'page': 'Layouts/layout_nav_bar.html', 'mensaje': e, 'alerta': 'Fallo'})
    else:
        return render(request, 'Methods_Templates/secante.html',
                      {'page': 'Layouts/layout_nav_bar.html', 'titulo': 'Secante', 'alerta': 'Melo'})

def biseccion(request):
    if request.method == 'GET':
        return render(request,'Methods_Templates/biseccion.html',
                      {'titulo': 'biseccion', 'alerta': 'Melo'})
    #Valores de entrada: Fx, x0, xi, tol, niter
    if request.method == 'POST' and 'latexinput' in request.POST:
        try:
            expression = request.POST['latexinput']
            tol = float(request.POST['toleranciam'])
            a = float(request.POST['a'])
            b = float(request.POST['b'])
            k = int(request.POST['iteracionm'])
        

            tupla = Biseccion.biseccion(expression, a, b, tol, k)
            return render(request, 'Methods_Templates/biseccion.html',
                          {'page': 'Layouts/layout_nav_bar.html', 'expresion': 'Biseccion', 'html': tupla[0], 'mensaje_m': tupla[1]})
        except ValueError as e:
            return render(request, 'Methods_Templates/biseccion.html',
                          {'page': 'Layouts/layout_nav_bar.html', 'mensaje': e, 'alerta': 'Fallo'})
    else:
        return render(request, 'Methods_Templates/biseccion.html',
                      {'page': 'Layouts/layout_nav_bar.html', 'titulo': 'Biseccion', 'alerta': 'Melo'})


#------------------ Vistas del segundo capitulo-----------------------

def doolittle(request):
    if request.method == 'POST':
        rows = int(request.POST.get('rows'))
        cols = int(request.POST.get('cols'))
        
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                val = request.POST.get(f'cell_{i}_{j}')
                row.append(int(val) if val else 0)
            matrix.append(row)
        
        # Llamada a la función doolittle
        result = Doolitle.doolittle_function(matrix)

        return render(request, 'Methods_Templates/doolitle.html', {'matrix': matrix, 'result': result})

    return render(request, 'Methods_Templates/doolitle.html')


def choleski(request):
    if request.method == 'POST':
        rows = int(request.POST.get('rows'))
        cols = int(request.POST.get('cols'))
        
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                val = request.POST.get(f'cell_{i}_{j}')
                row.append(int(val) if val else 0)
            matrix.append(row)
        result = Choleski.choleski(matrix)

        return render(request, 'Methods_Templates/Choleski.html', {'matrix': matrix, 'result': result})

    return render(request, 'Methods_Templates/Choleski.html')