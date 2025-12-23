# 📸 FaceVision

O **FaceVision** é uma aplicação web robusta desenvolvida para automatizar o controle de frequência escolar. Utilizando tecnologia de reconhecimento e gestão de dados, o sistema substitui as chamadas manuais tradicionais, reduzindo falhas e auxiliando na gestão de notas e combate à evasão escolar.

<p align="left">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
</p>

## 🎯 Sobre o Projeto

O objetivo principal é oferecer aos professores uma ferramenta centralizada para registro de avaliações e frequência, permitindo que a gestão escolar tenha uma visão clara do desempenho e presença dos alunos em tempo real.

### 🚀 Principais Funcionalidades

- **Controle de Frequência Automatizado:** Registro inteligente de presença.
- **Gestão de Notas:** Lançamento e acompanhamento de boletins escolares.
- **Painel Administrativo:** Interface para controle total de usuários, turmas e horários.
- **Módulos Específicos:** Áreas dedicadas para Minhas Avaliações, Horários e Dados do Usuário.

## 📂 Estrutura do Projeto

O projeto segue a arquitetura **MTV (Model-Template-View)** do Django:

* **Facevision/**: Core da aplicação (Models, Views e lógica de negócio).
* **static/**: Arquivos de estilo (CSS), interatividade (JS) e recursos visuais (Img).
* **templates/**: Estruturas HTML organizadas por módulos (Login, Cadastro, Boletim, etc).
* **dados_usuarios/**: Armazenamento local de perfis em formato JSON.
* **manage.py**: Script de gerenciamento do ecossistema Django.

## 🛠️ Tecnologias Utilizadas

- **Backend:** [Python](https://www.python.org/) & [Django Framework](https://www.djangoproject.com/)
- **Frontend:** HTML5, CSS3 e Bootstrap e JavaScript
- **Banco de Dados:** SQLite (Desenvolvimento)

## 📺 Demonstração

https://github.com/user-attachments/assets/7aa1c6a7-875c-483e-9289-936602c0e87b


## 🔧 Configuração e Instalação

Siga os passos para rodar o projeto localmente:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/RayssaVicente/Facevision.git](https://github.com/RayssaVicente/Facevision.git)
   
   cd Facevision

2. **Ative o venv:**
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   
   # Linux/Mac:
   source venv/bin/activate
   
4. **Instale todas as depedencias necessarias:**
   pip install -r requirements.txt

   python manage.py migrate
   python manage.py runserver
   
5. **Acesse o servidor local**
   http://127.0.0.1:8000/
