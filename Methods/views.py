from django.http import HttpResponse
from django.shortcuts import render, redirect
from .PCM import Regla_Falsa, Busqueda_incremental, Newton_rapshon, Multiple_Roots, Fixed_Point, Doolitle, Secante, Biseccion, Choleski, Crout, SOR, Gauss_Seidel


# -------------------------------------- Homepage --------------------------------------
def home_view(request):
    if request.method == 'GET':
        return render(request,'Methods_Templates/Home.html',
                              {'page': 'Layouts/layout_nav_bar.html', 'titulo': 'Home', 'alerta': 'Melo'})


# --------------------------------------- Graph --------------------------------------
def graph(request):
    if request.method == 'GET':
        return render(request,'Methods_Templates/Graph.html',
                              {'titulo': 'Grafica', 'alerta': 'Melo'})
    if request.method == 'POST':
        return render(request, 'Methods_Templates/Graph.html',
                      {'titulo': 'Grafica', 'alerta': 'Melo'})


# --------------------------------------- Methods --------------------------------------
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

def fixed_point(request):
    if request.method == 'GET':
        return render(request,'Methods_Templates/FixedPoint.html',
                      {'titulo': 'Punto Fijo', 'alerta': 'Melo'})
    if request.method == 'POST' and 'latexinput' in request.POST:
        try:
            expression = request.POST['latexinput']
            tol = float(request.POST['toleranciam'])
            x0 = float(request.POST['xi'])
            nmax = int(request.POST['iteracionm'])
            et = request.POST['tipoe']

            tupla = Fixed_Point.fixed_point(expression, x0, tol, nmax, et)
            return render(request, 'Methods_Templates/FixedPoint.html',
                          {'page': 'Layouts/layout_nav_bar.html', 'expression': 'Punto Fijo', 'html': tupla[0], 'mensaje_m': tupla[1]})
        except ValueError as e:
            return render(request, 'Methods_Templates/FixedPoint.html',
                          {'page': 'Layouts/layout_nav_bar.html', 'mensaje': e, 'alerta': 'Fallo'})
    else:
        return render(request, 'Methods_Templates/FixedPoint.html',
                      {'page': 'Layouts/layout_nav_bar.html', 'titulo': 'Punto Fijo', 'alerta': 'Melo'})
    
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


#----------------------------- Views of the second chapter ------------------------------
def doolittle(request):
    if request.method == 'POST':
        rows = float(request.POST.get('rows'))
        cols = float(request.POST.get('cols'))
        
        matrix = []
        for i in range(int(rows)):
            row = []
            for j in range(int(cols)):
                val = request.POST.get(f'cell_{i}_{j}')
                row.append(float(val) if val else 0.0)
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

def crout(request):
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

        result = Crout.crout(matrix)

        return render(request, 'Methods_Templates/Crout.html', {'matrix': matrix, 'result': result})

    return render(request, 'Methods_Templates/Crout.html')


def SOR_method(request):
    if request.method == 'POST':
        rows = int(float(request.POST['rows']))
        cols = int(float(request.POST['cols']))
        tol = float(request.POST['Tol'])
        niter = int(request.POST['niter'])
        w = float(request.POST['w'])

        siFallo = False

        A = []
        for i in range(rows):
            row = []
            for j in range(cols):
                cell_name = f'A_{i}_{j}'
                cell_value = float(request.POST[cell_name])
                row.append(cell_value)
            A.append(row)

        # Obtener el vector b
        b = []
        for i in range(int(rows)):
            cell_name = f'b_{i}'
            cell_value = float(request.POST[cell_name])
            b.append(cell_value)

        # Obtener el vector x0
        x0 = []
        for i in range(int(rows)):
            cell_name = f'x0_{i}'
            cell_value = float(request.POST[cell_name])
            x0.append(cell_value)

        result = SOR.SOR(x0, A, b, tol, niter, w)
        context = {
            'result_vector': result[0],
            'iterations': result[1],
        }

        if (result[1] > niter):
            siFallo = True

        return render(request, 'Methods_Templates/SOR.html', {'context': context, 'siFallo': siFallo})

    return render(request, 'Methods_Templates/SOR.html')

def gauss_seidel(request):
    if request.method == 'POST':
        try:
            rows = int(request.POST.get('rows'))

            # Obtener valores de la matriz
            matrix = []
            for i in range(rows):
                row = []
                for j in range(rows):
                    val = request.POST.get(f'cell_{i}_{j}')
                    row.append(int(val) if val else 0)
                matrix.append(row)

            # Obtener valores del vector B
            vector_b = []
            for i in range(rows):
                val = request.POST.get(f'b_{i}')
                vector_b.append(int(val) if val else 0)

            # Obtener valores del vector X0
            vector_x0 = []
            for i in range(rows):
                val = request.POST.get(f'x0_{i}')
                vector_x0.append(int(val) if val else 0)

            tol = float(request.POST.get('tol'))
            iter = int(request.POST.get('iter'))

            result = Gauss_Seidel.Gauss_Seidel(matrix, vector_b, vector_x0, tol, iter)

            return render(request, 'Methods_Templates/GausSeidel.html',
                          {'result': result})
        except:
            return render(request, 'Methods_Templates/GausSeidel.html',
                          {'mensaje_m': 'Error en los datos ingresados'})

    return render(request, 'Methods_Templates/GausSeidel.html')
