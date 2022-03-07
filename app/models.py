from django.db import models

# Create your models here.

class usuario(models.Model):
    matricula = models.IntegerField()
    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=50)
    funcao = models.CharField(max_length=50)
    mobile = models.IntegerField()
    caf = models.CharField(max_length=50)
    armario = models.IntegerField()
    chave = models.IntegerField()