from django.db import models

class aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cidade = models.CharField(max_length=100)

