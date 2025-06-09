from django.contrib import admin
from django.urls import path
from Facevision.views import home, cadastro, salvar_dados, login_view, boletin,dadosUsuario, horarios, minhasAvaliacoes, user_logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Página inicial carregando o template HTML
    path('cadastro/', cadastro, name='cadastro'), #carrega a pagina htm cadastro
    path('salvar-dados/', salvar_dados, name='salvar_dados'),
    path('login/', login_view, name='login'),
    path('boletin/', boletin, name='boletin'),
    path('dadosUsuario/', dadosUsuario, name='dadosUsuario'),
    path('horarios/', horarios, name='horarios'),
    path('minhasAvaliacoes/', minhasAvaliacoes, name='minhasAvaliacoes'),
    path('logout/', user_logout, name='logout')

]
