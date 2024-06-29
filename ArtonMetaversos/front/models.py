from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Raça
class Raca(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    atributos = models.CharField(max_length=255)  # Por exemplo, 'Força: 10, Destreza: 8, etc.'
    habilidades = models.CharField(max_length=255)  # Por exemplo, 'Visão no Escuro, Resistência a Veneno, etc.'
    logica_de_criacao = models.JSONField(default=dict)  # Define um valor padrão
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona com o usuário que criou a raça
    versao = models.CharField(max_length=10, default='1.0')  # Versão inicial

    def __str__(self):
        return self.nome