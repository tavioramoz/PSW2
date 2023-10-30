from django.urls import path

from . import views

urlpatterns = [
    path("tavio/", views.index, name="index"),
]