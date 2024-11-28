from django.urls import path
from proveedores_app import views

urlpatterns = [
    path("Proveedores", views.inicio_vistaProveedores, name="Proveedores"),
    path("registrarPro/", views.registrarPro, name="registrarPro"),
    path("seleccionarPro/<codigo>", views.seleccionarPro, name="selecionarPro"),
    path("editarPro/", views.editarPro, name="editarPro"),
    path("borrarPro/<codigo>", views.borrarPro, name="borrarPro")
    ]
