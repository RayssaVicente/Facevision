from django.contrib import admin
from django.urls import path
from Facevision.views import home, cadastro



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Página inicial carregando o template HTML
    path('cadastro/', cadastro, name='cadastro'),
]
