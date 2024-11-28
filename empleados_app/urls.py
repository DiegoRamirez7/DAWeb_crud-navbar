from django.urls import path
from empleados_app import views

urlpatterns = [
    path("Empleados", views.inicio_vistaEmpleados, name="Empleados"),
    path("registrarEmp/", views.registrarEmp, name="registrarEmp"),
    path("seleccionarEmp/<codigo>", views.seleccionarEmp, name="selecionarEmp"),
    path("editarEmp/", views.editarEmp, name="editarEmp"),
    path("borrarEmp/<codigo>", views.borrarEmp, name="borrarEmp")
    ]
