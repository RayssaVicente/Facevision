from django.shortcuts import render
import os
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

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
        dados_usuario = {
            "nome": nome,
            "email": email,
            "senha": senha, 
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
    return HttpResponse("Usuário cadastrado com sucesso!", content_type="text/plain") 


#basicamente ele não tá salvando os dados no json, so ta exibindo a mensagem
#mais tá tudo feito pra dar cert já so falta melhorar essa função para dra certo

