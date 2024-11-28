from django.urls import path
from categorias_app import views

urlpatterns = [
    path("Categorias", views.inicio_vistaCategorias, name="Categoria"),
    path("registrarCat/", views.registrarCat, name="registrarCat"),
    path("seleccionarCat/<codigo>", views.seleccionarCat, name="selecionarCat"),
    path("editarCat/", views.editarCat, name="editarCat"),
    path("borrarCat/<codigo>", views.borrarCat, name="borrarCat")
    ]
