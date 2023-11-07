
from django.http import HttpResponse
from django.shortcuts import render

from  .models import aluno


def create(request, id_aluno):
    return HttpResponse("<h1> Aqui cria </h1>")

def read(request, id_aluno):
    return HttpResponse("<h1> Aqui lista </h1>")

def update(request, id_aluno):
    return HttpResponse("<h1> Aqui atualiza </h1>")

def delete(request, id_aluno):
    return HttpResponse("<h1> Aqui apaga:" + str(id_aluno) + "<h/1>")

def detail(request, id_aluno):

    saida = Aluno.objects.get(pk=id_aluno)
    template =loader.get_template("index.html")

     return HttpResponse(template.reader({}))