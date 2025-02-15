from django.shortcuts import render

def home(request):
    return render(request, 'login/index.html')

def cadastro(request):
    return render(request, 'cadastro/index.html')
