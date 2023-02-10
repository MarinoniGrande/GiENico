from django.db import models


# Create your models here.
class Evento(models.Model):
    status = models.CharField(max_length=1, null=True)
    nome = models.CharField(max_length=200, null=True)
    data = models.CharField(max_length=50, null=True)
    descricao = models.CharField(max_length=500, null=True)
    imagem = models.CharField(max_length=200, null=True)


class Motivo(models.Model):
    tipo = models.CharField(max_length=200, null=True)
    nome = models.CharField(max_length=200, null=True)


class Configuracao(models.Model):
    tipo = models.CharField(max_length=200, null=True)
    valor = models.TextField(null=True)


class Pagina(models.Model):
    url = models.CharField(max_length=200, null=True)
    conteudo = models.TextField(null=True)