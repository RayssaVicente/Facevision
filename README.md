# FaceVision

Este repositório contém o código-fonte de uma aplicação web desenvolvida para automatizar o controle de frequência de alunos, substituindo métodos tradicionais e suscetíveis a falhas, como a chamada manual e o uso de listas de papel. O sistema também conta com um site onde vai ser possível colocar as notas e dados do aluno.

## Sobre o Projeto

A aplicação "FaceVision" é construída utilizando o framework web Django no backend, e tecnologias web padrão como HTML, CSS e JavaScript no frontend. O objetivo principal é ajudar os professores no registro de notas e frequência, e a gestão escolar no controle de evasão escolar.
### Estrutura do Projeto

O projeto é organizado da seguinte forma:

* *Facevision/*: Contém a lógica principal da aplicação web, incluindo:
    * *models.py*: Definição dos modelos de dados (estruturas do banco de dados).
    * *views.py*: Lógica de negócios e controle das requisições HTTP.
    * *admin.py*: Configurações para a interface de administração do Django.
    * *migrations/*: Arquivos de migração do banco de dados.
* *estático/*: Armazena os arquivos estáticos da aplicação (CSS, JavaScript, Imagens):
    * *Css/*: Estilos CSS para o design da interface.
    * *img/*: Imagens utilizadas na aplicação (fundos, logos, fotos de usuário).
    * *Js/*: Scripts JavaScript para interatividade no frontend.
* *Modelos/*: Contém os arquivos HTML (templates) para as diferentes seções da aplicação:
    * boletin/, cadastro/, dados-usuario/, Horarios/, login/, minhas-avaliacoes/, principal/: Cada pasta provavelmente representa uma página ou um módulo específico da interface do usuário.
* *dados_usuarios/*: Possivelmente armazena dados de usuários em formato JSON.
* *db.sqlite3*: O banco de dados SQLite utilizado para desenvolvimento.
* *venv/*: Ambiente virtual Python para gerenciar as dependências do projeto.
* *manage.py*: Script de linha de comando do Django para gerenciar o projeto.

## Tecnologias Utilizadas

* *Backend*: Python, Django
* *Frontend*: HTML5, CSS3, JavaScript

## Como Configurar e Rodar o Projeto (Instruções para Desenvolvimento)

Para configurar e rodar este projeto em seu ambiente local, siga os passos abaixo:

1.  *Clone o repositório:*

    bash
    git clone [https://github.com/RayssaVicente/Visao-facial.git](https://github.com/RayssaVicente/Visao-facial.git) # Verifique o URL exato do seu repositório
    cd FaceVision
    

2.  *Crie e ative o ambiente virtual:*

    bash
    python -m venv venv
     No Windows:
    .\venv\Scripts\activate
     No macOS/Linux:
    source venv/bin/activate
    

3.  *Instale as dependências:*

    bash
    pip install -r requirements.txt # Você precisará criar este arquivo se ainda não existir
    
    * *Nota*: Se o requirements.txt não existir, você precisará criá-lo com as dependências do Django e quaisquer outras que você esteja usando (ex: pip freeze > requirements.txt após instalar tudo). Pelo menos, Django será necessário.

4.  *Execute as migrações do banco de dados:*

    bash
    python manage.py makemigrations
    python manage.py migrate
    

5.  *Crie um superusuário (opcional, para acessar o admin do Django):*

    bash
    python manage.py createsuperuser
    

6.  *Inicie o servidor de desenvolvimento:*

    bash
    python manage.py runserver
    

    A aplicação estará acessível em http://127.0.0.1:8000/.

## Como Usar

[*Descreva aqui os passos básicos para usar a aplicação uma vez que ela esteja rodando. Por exemplo:*
* "Acesse a página de login em /login."
* "Navegue para a página de cadastro em /cadastro para criar uma nova conta."
* "Explore as funcionalidades do sistema."
]
