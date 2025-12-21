from django.db import models
from django.contrib.auth.hashers import make_password

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)  # Guardará a senha já criptografada
    curso = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        # Garante que a senha seja salva já criptografada
        self.senha = make_password(self.senha)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


from django.db import models
from django.contrib.auth.models import User

class Avaliacao(models.Model):
    professor = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_aluno = models.CharField(max_length=100)
    materia = models.CharField(max_length=50)
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    data_lancamento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_aluno} - {self.nota}"

    




# Create your models here.
