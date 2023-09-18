from django.shortcuts import render, redirect

# Create your views here.
def false_rule(request):
    if request.method == 'GET':
        return render(request, 'Methods_Templates/FalseRule.html')
