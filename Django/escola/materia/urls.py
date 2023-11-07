from django.urls import path

from . import views

urlpatterns = [
    path("add/", views.create, name="adicionar"),
     path("", views.read, name="ler"),
      path("update/", views.update, name="atualizar"),
       path("<int:id_aluno>/delete", views.delete, name="deletar"),
         path("<int:id_aluno>/detail", views.detail, name="detalha"),

]