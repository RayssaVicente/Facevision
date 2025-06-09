from django.shortcuts import render, redirect
import os
import json
import re
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout


# Função para garantir que a pasta e o arquivo existem
def verificar_pasta():
    caminho_pasta = os.path.join(settings.BASE_DIR, "dados_usuarios")
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
    return os.path.join(caminho_pasta, "dados.json")


# Função para carregar usuários do JSON
def carregar_usuarios():
    caminho_arquivo = verificar_pasta()
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Função para salvar usuários no JSON
def salvar_usuarios(dados):
    caminho_arquivo = verificar_pasta()
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


# Página inicial
def home(request):
    return  render(request, 'login/index.html')


# Página de cadastro (formulário)
def cadastro(request):
    return render(request, 'cadastro/index.html')


# Função para salvar usuário no JSON
def salvar_dados(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')  
        curso = request.POST.get('curso')

        # Validação de senha
        senha_valida = re.fullmatch(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%#*?&]{8,}$', senha)
        if not senha_valida:
            return render(request, 'cadastro/index.html', {
                'mensagem': 'A senha deve ter pelo menos 8 caracteres, uma letra maiúscula, um número e um caractere especial.',
                'tipo': 'erro'
            })

        senha_hash = make_password(senha)

        # Carrega usuários do JSON
        dados_usuarios = carregar_usuarios()

        for usuario in dados_usuarios:
            if usuario["email"] == email:
                return render(request, 'cadastro/index.html', {
                    'mensagem': 'E-mail já cadastrado!',
                    'tipo': 'erro'
                })

        novo_usuario = {
            "nome": nome,
            "email": email,
            "senha": senha_hash,
            "curso": curso
        }
        dados_usuarios.append(novo_usuario)
        salvar_usuarios(dados_usuarios)

        return render(request, 'cadastro/index.html', {
            'mensagem': 'Usuário cadastrado com sucesso!',
            'tipo': 'sucesso'
        })

    return render(request, 'cadastro/index.html', {
        'mensagem': 'Método não permitido.',
        'tipo': 'erro'
    })


# Função de login
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        dados_usuarios = carregar_usuarios()

        for usuario in dados_usuarios:
            if usuario["email"] == email:
                if check_password(senha, usuario["senha"]):
                    return render(request, 'principal/index.html')
                else:
                    return render(request, 'login/index.html', {
                        'erro': 'Senha incorreta'
                    })

        return render(request, 'login/index.html', {
            'erro': 'E-mail não encontrado!'
        })
    else:
        return render(request, 'login/index.html')

def boletin(request):
    return render(request, 'boletin/index.html')

def dadosUsuario(request):
    return render(request, 'dados-usuario/index.html')

def horarios(request):
    return render(request, 'horarios/index.html')

def minhasAvaliacoes(request):
    return render(request, 'minhas-avaliacoes/index.html')

def user_logout(request):
    logout(request)  
    return redirect('login') 

