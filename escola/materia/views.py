from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .forms import AlunoForm
from .models import aluno


def criar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        form.save()
        return HttpResponseRedirect('/materia/?msg=Salvo!')
    else:
        form = AlunoForm()
    return render(request, "materia/formAluno.html", {'form' : form})

def listarTudo(request):
    
    alunos = aluno.objects.all()
    
    return render(request, "materia/listarTudo.html", {'aluno' : alunos}) 

def editar(request, id_aluno):
    return HttpResponse("<h1> Aqui atualiza" +str(id_aluno)+ "</h1>")

def deletar(request, id_aluno):
    return HttpResponse("<h1> Aqui apaga:" +str(id_aluno)+ "</h1>")

def detalhar(request, id_aluno):
    
    try:
     saida = aluno.objects.get(pk=id_aluno)
     
    except:
     saida = "Aqui não tem aluno!"
     
    return render(request, "materia/index.html",{'aluno': saida})
    





