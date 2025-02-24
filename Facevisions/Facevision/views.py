from django.shortcuts import render, redirect
import os
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import re
from django.contrib.auth.hashers import make_password, check_password


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

        try: #recuperar os dados
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                dados_existentes = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            dados_existentes = []
        dados_existentes.append(dados_usuario)
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo: #salvar os dados
            json.dump(dados_existentes, arquivo, indent=4, ensure_ascii=False)
    return HttpResponse("Usuario cadastrado com sucesso!", content_type="text/plain") 
def login_view(request):
    if request.method== "POST":

        email = request.POST.get('email')
        senha = request.POST.get('senha')
        caminho_pasta = os.path.join(settings.BASE_DIR, "dados_usuarios")
        caminho_arquivo = os.path.join(caminho_pasta, "dados.json")
        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                dados_usuarios = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            dados_usuarios = []
        
        for usuario in dados_usuarios:
            if usuario["email"] == email:
                if check_password(senha,usuario["senha"]):
                    return HttpResponse("Login realizado com sucesso!", content_type="text/plain")
                else:
                    return HttpResponse("senha incorreta", content_type="text/plain")
        else:
            return HttpResponse("email nao encontrado!", content_type='text/plain')
    return render(request, 'login/index.html')


#basicamente ele não tá salvando os dados no json, so ta exibindo a mensagem
#mais tá tudo feito pra dar cert já so falta melhorar essa função para dra certo

