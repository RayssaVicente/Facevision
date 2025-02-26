from django.shortcuts import render, redirect
import os
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import re
from django.contrib.auth.hashers import make_password, check_password
from .models import Aluno



def home(request):
    return render(request, 'login/index.html')

def cadastro(request):
    return render(request, 'cadastro/index.html')

def salvar_dados(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')  
        curso = request.POST.get('curso')
        senha_valida = re.fullmatch(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%#*?&]{8,}$', senha)
        if not senha_valida:
            return HttpResponse("A senha deve ter pelo menos 8 caracteres, uma letra maiuscula, um numero e um caractere especial.", content_type="text/plain")
        senha_hash = make_password(senha)

        dados_usuario = {
            "nome": nome,
            "email": email,
            "senha": senha_hash, 
            "curso": curso
        }
        caminho_pasta = os.path.join(settings.BASE_DIR, "dados_usuarios")
        caminho_arquivo = os.path.join(caminho_pasta, "dados.json")

        try:
            aluno = Aluno(nome=nome, email=email, senha=senha, curso=curso)
            aluno.save()
            return HttpResponse("Usuário cadastrado com sucesso!", content_type="text/plain")
        except:
            return HttpResponse("Erro ao cadastrar. O e-mail pode já estar cadastrado.", content_type="text/plain")

       
    return HttpResponse("Usuario cadastrado com sucesso!", content_type="text/plain") 
    
def login_view(request):
    if request.method== "POST":

        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            usuario = Aluno.objects.get(email=email)  # Busca pelo e-mail
            if check_password(senha, usuario.senha):  # Verifica a senha
                return HttpResponse("Login realizado com sucesso!", content_type="text/plain")
            else:
                return HttpResponse("Senha incorreta", content_type="text/plain")
        except Aluno.DoesNotExist:
            return HttpResponse("E-mail não encontrado!", content_type="text/plain")
  
        
    return render(request, 'login/index.html')


