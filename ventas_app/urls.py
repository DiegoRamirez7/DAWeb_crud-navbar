from django.urls import path
from ventas_app import views

urlpatterns = [
    path("Venta", views.inicio_vistaVentas, name="Venta"),
    path("registrarVenta/", views.registrarVenta, name="registrarVenta"),
    path("seleccionarVenta/<codigo>", views.seleccionarVenta, name="selecionarVenta"),
    path("editarVentas/", views.editarVentas, name="editarVentas"),
    path("borrarVenta/<codigo>", views.borrarVenta, name="borrarVenta")
    ]
