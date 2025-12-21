from django.contrib import admin
from django.urls import path
from Facevision.views import home, cadastro, salvar_dados, login_view, boletin,dadosUsuario, horarios, minhasAvaliacoes, user_logout,editar_perfil, telaProfessor, salvar_nota,perfil_professor,minhas_notas,agendar_avaliacao, principal


urlpatterns = [
    path('admin/', admin.site.urls),
    
# telas dos pro
    path('', home),  # Página inicial carregando o template HTML
    path ('principal/', principal, name="principal"),
    path('boletin/', boletin, name='boletin'),
    path('dadosUsuario/', dadosUsuario, name='dadosUsuario'),
    path('horarios/', horarios, name='horarios'),
    path('minhasAvaliacoes/', minhasAvaliacoes, name='minhasAvaliacoes'),
    path('logout/', user_logout, name='logout'),
    path('cadastro/', cadastro, name='cadastro'),
    path('salvar_dados/', salvar_dados, name='salvar_dados'),
    path('login/', login_view, name='login_view'),
    path('editar-perfil/', editar_perfil, name='editar_perfil'),
    path('minhas_notas/', minhas_notas, name='minhas_notas'),

# telas dos professores
    path('telaProfessor/', telaProfessor, name='telaProfessor'),
    path('professor/salvar-nota/', salvar_nota, name='salvar_nota'),
    path('professor/perfil/', perfil_professor, name='perfil_professor'),
    path('professor/agendar_avaliacao/', agendar_avaliacao, name='agendar_avaliacao'),
    


]
