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

    




# Create your models here.
