from django.urls import path

from . import views

urlpatterns = [
    path ("add/", views.criar, name="add"),
    path ("", views.listarTudo, name="listar"),
    path ("editar/<int:id_aluno>/", views.editar, name="atualizar"),
    path ("deletar/<int:id_aluno>/", views.deletar, name="deletar"),
    path ("detalhar/<int:id_aluno>/", views.detalhar, name="detalhar")

]



