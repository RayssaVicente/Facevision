from django.contrib import admin
from django.urls import path
from Facevision.views import home, cadastro, salvar_dados, login_view





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Página inicial carregando o template HTML
    path('cadastro/', cadastro, name='cadastro'), #carrega a pagina htm cadastro
    path('salvar-dados/', salvar_dados, name='salvar_dados'),
    path('login/', login_view, name='login'),# carrega a função de salvar dados, mais não está salvando 
]
