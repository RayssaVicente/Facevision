from django.shortcuts import render, redirect
import os
import json
import re
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout 
from datetime import datetime

# --- CONFIGURAÇÃO DE CAMINHOS ---
PATH_DADOS = os.path.join(settings.BASE_DIR, 'dados_usuarios')
# Garante que a pasta existe ao iniciar o servidor
if not os.path.exists(PATH_DADOS):
    os.makedirs(PATH_DADOS)

PATH_LOGIN_ALUNOS = os.path.join(PATH_DADOS, 'usuarios_login.json')
PATH_PERFIS_ALUNOS = os.path.join(PATH_DADOS, 'perfis_alunos.json')
PATH_LOGIN_PROFS = os.path.join(PATH_DADOS, 'professores_login.json')
PATH_NOTAS = os.path.join(PATH_DADOS, 'notas.json')
PATH_AGENDA = os.path.join(PATH_DADOS, 'agenda.json')

# --- FUNÇÕES AUXILIARES ---
def carregar_json(caminho):
    if not os.path.exists(caminho):
        return []
    with open(caminho, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_json(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# --- VIEWS DE NAVEGAÇÃO ---
def home(request):
    return render(request, 'login/index.html')

def principal(request):
    return render(request, 'principal/index.html')


def cadastro(request):
    return render(request, 'cadastro/index.html')

# --- LÓGICA DE CADASTRO ---
def salvar_dados(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        curso = request.POST.get('curso')
        serie_inicial = request.POST.get('periodo') 
        ano_ingresso = datetime.now().year

        # 1. Validação de Senha
        regex_senha = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%#*?&]{8,}$'
        if not re.fullmatch(regex_senha, senha):
            return render(request, 'cadastro/index.html', {'mensagem': 'Senha inválida.', 'tipo': 'erro'})

        # 2. Verificar Duplicidade
        usuarios_login = carregar_json(PATH_LOGIN_ALUNOS)
        if any(u['email'] == email for u in usuarios_login):
            return render(request, 'cadastro/index.html', {'mensagem': 'E-mail já cadastrado!', 'tipo': 'erro'})

        # 3. Salvar Login (Com Hash)
        novo_login = {"email": email, "senha": make_password(senha)}
        usuarios_login.append(novo_login)
        salvar_json(PATH_LOGIN_ALUNOS, usuarios_login)

        # 4. Salvar Perfil
        perfis_alunos = carregar_json(PATH_PERFIS_ALUNOS)
        novo_perfil = {
            "email": email, 
            "nome_completo": nome,
            "curso": curso,
            "serie_ingresso": int(serie_inicial),
            "ano_ingresso": ano_ingresso,
            "status": "Matriculado"
        }
        perfis_alunos.append(novo_perfil)
        salvar_json(PATH_PERFIS_ALUNOS, perfis_alunos)

       # No final da função salvar_dados:
    return render(request, 'login/index.html', {
        'mensagem': 'Conta criada com sucesso! Redirecionando...', 
        'tipo': 'sucesso'
    })

# --- LÓGICA DE LOGIN ---
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # TENTA PROFESSOR
        professores = carregar_json(PATH_LOGIN_PROFS)
        for prof in professores:
            if prof["email"] == email:
                if prof["senha"] == senha: 
                    request.session['usuario_email'] = email
                    request.session['tipo_usuario'] = 'professor'
                    return redirect('telaProfessor')
                else:
                    return render(request, 'login/index.html', {'erro': 'Senha de professor incorreta'})

        # TENTA ALUNO
        alunos = carregar_json(PATH_LOGIN_ALUNOS)
        for aluno in alunos:
            if aluno["email"] == email:
                if check_password(senha, aluno["senha"]):
                    request.session['usuario_email'] = email
                    request.session['tipo_usuario'] = 'aluno'
                    return redirect('principal')
                else:
                    return render(request, 'login/index.html', {'erro': 'Senha de aluno incorreta'})

        return render(request, 'login/index.html', {'erro': 'E-mail não encontrado!'})
    return render(request, 'login/index.html')

# --- ÁREA DO ALUNO ---
def dadosUsuario(request):
    email_logado = request.session.get('usuario_email')
    if not email_logado: return redirect('/')

    perfis = carregar_json(PATH_PERFIS_ALUNOS)
    perfil = next((p for p in perfis if p['email'] == email_logado), None)

    if perfil:
        ano_atual = datetime.now().year
        serie_calculada = (ano_atual - perfil['ano_ingresso']) + perfil['serie_ingresso']
        perfil['serie_exibicao'] = f"{serie_calculada}º ano Ensino Médio" if serie_calculada <= 3 else "Concluiu"
        return render(request, 'dados-usuario/index.html', {'aluno': perfil})
    return redirect('/')


def boletin(request):
    return render(request, 'boletin/index.html')

def horarios(request):
    return render(request, 'horarios/index.html')

def minhasAvaliacoes(request):
    # Carrega os dados do seu arquivo JSON de agenda/provas
    agenda_data = carregar_json(PATH_AGENDA) 
    
    # Passa a lista para o template com o nome 'avaliacoes'
    return render(request, 'minhas-avaliacoes/index.html', {'avaliacoes': agenda_data})

def editar_perfil(request):
    if request.method == "POST":
        email_logado = request.session.get('usuario_email')
        perfis = carregar_json(PATH_PERFIS_ALUNOS)
        for perfil in perfis:
            if perfil['email'] == email_logado:
                perfil['nome_completo'] = request.POST.get('nome')
                perfil['curso'] = request.POST.get('curso')
                perfil['serie_ingresso'] = int(request.POST.get('periodo'))
                break
        salvar_json(PATH_PERFIS_ALUNOS, perfis)
    return redirect('dadosUsuario')

# --- ÁREA DO PROFESSOR ---
def telaProfessor(request):
    email_logado = request.session.get('usuario_email')
    professores = carregar_json(PATH_LOGIN_PROFS)
    prof = next((p for p in professores if p['email'] == email_logado), None)
    
    if not prof: return redirect('/')

    todos_alunos = carregar_json(PATH_PERFIS_ALUNOS)
    turmas_do_prof = prof.get('turmas', [])
    alunos_filtrados = [a for a in todos_alunos if int(a.get('serie_ingresso')) in turmas_do_prof]

    return render(request, 'professor/index.html', {
        'alunos': alunos_filtrados,
        'materia': prof.get('materia', 'Sua Matéria')
    })

def salvar_nota(request):
    if request.method == "POST":
        nota_bruta = request.POST.get('valor_nota')
        aluno_email = request.POST.get('aluno_id')
        nome_avaliacao = request.POST.get('nome_avaliacao') # Novo campo do form
        
        # Pega os dados do professor logado para saber a matéria
        professores = carregar_json(PATH_LOGIN_PROFS)
        prof_logado = next((p for p in professores if p['email'] == request.session.get('usuario_email')), None)
        materia = prof_logado.get('materia', 'Geral') if prof_logado else "Geral"

        if not nota_bruta: return HttpResponse("Nota inválida.")
        
        notas = carregar_json(PATH_NOTAS)
        notas.append({
            "aluno_email": aluno_email,
            "professor_email": request.session.get('usuario_email'),
            "disciplina": materia,      # Adicionado
            "avaliacao": nome_avaliacao, # Adicionado
            "nota": float(nota_bruta),
            "data": datetime.now().strftime("%d/%m/%Y")
        })
        salvar_json(PATH_NOTAS, notas)
        return redirect('telaProfessor')

def perfil_professor(request):
    email_logado = request.session.get('usuario_email')
    professores = carregar_json(PATH_LOGIN_PROFS)
    prof = next((p for p in professores if p['email'] == email_logado), None)
    if not prof: return redirect('/')
    return render(request, 'professor/perfil.html', {'professor': prof})

def minhas_notas(request):
    email_logado = request.session.get('usuario_email')
    
    if not email_logado:
        return redirect('/')

    # Normaliza o email para evitar erros de digitação (minúsculas e sem espaços)
    email_logado = email_logado.strip().lower()

    todas_notas = carregar_json(PATH_NOTAS)
    
    # Filtra comparando ambos em minúsculo
    notas_do_aluno = [
        n for n in todas_notas 
        if str(n.get('aluno_email')).strip().lower() == email_logado
    ]

    notas_do_aluno.reverse()

    return render(request, 'minhas-notas/index.html', {'avaliacoes': notas_do_aluno})


def obter_calendario_avaliacoes(request):
    """
    Função para carregar o calendário de avaliações do arquivo JSON.
    """
    # Caminho para o seu arquivo de agenda (certifique-se que PATH_AGENDA está definido)
    caminho_agenda = os.path.join(settings.BASE_DIR, 'dados_usuarios', 'agenda.json')
    
    # 1. Carrega os dados brutos do JSON usando sua função auxiliar carregar_json
    agenda_completa = carregar_json(caminho_agenda)
    
    # 2. Se você quiser filtrar por aluno logado (exibir apenas provas da turma dele):
    email_logado = request.session.get('usuario_email')
    perfis = carregar_json(PATH_PERFIS_ALUNOS)
    aluno = next((p for p in perfis if p['email'] == email_logado), None)
    
    calendario_filtrado = []
    
    if aluno:
        for item in agenda_completa:
            # Filtra pela turma do aluno (ex: 1, 2 ou 3)
            if int(item.get('turma')) == int(aluno.get('serie_ingresso')):
                calendario_filtrado.append({
                    'nome_avaliacao': item.get('nome_avaliacao'),
                    'disciplina': item.get('disciplina'),
                    'data': item.get('data')
                })
    
    # 3. Retorna para o template
    return render(request, 'minhasAvaliacoes/index.html', {'avaliacoes': calendario_filtrado})

def agendar_avaliacao(request):
    if request.method == "POST":
        # Pega a matéria do professor logado
        professores = carregar_json(PATH_LOGIN_PROFS)
        prof_logado = next((p for p in professores if p['email'] == request.session.get('usuario_email')), None)
        materia = prof_logado.get('materia', 'Geral') if prof_logado else "Geral"

        agenda = carregar_json(PATH_AGENDA)
        nova_prova = {
            "disciplina": materia,
            "nome_avaliacao": request.POST.get('nome_prova'),
            "data": request.POST.get('data_prova'),
            "turma": int(request.POST.get('turma')), # 1, 2 ou 3
            "tipo": request.POST.get('tipo_prova'), # Ex: Prova Prática, Trabalho
            "area": request.POST.get('area_conhecimento') # Linguagens, Exatas, Humanas ou Biológicas
        }
        
        agenda.append(nova_prova)
        salvar_json(PATH_AGENDA, agenda)
        return redirect('telaProfessor')

def user_logout(request):
    logout(request)
    return redirect('/')