from django.shortcuts import render, redirect
from .models import Clientes
# Create your views here.

def inicio_vistaClientes(request):
    lasClientes=Clientes.objects.all

    return render(request,"gestionarClientes.html", {"misclientes":lasClientes})

def registrarCliente(request):
    codigo=request.POST["txtcodigo"] 
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    correo=request.POST["txtcorreo"]
    fecha=request.POST["txtfecha"]
    tipo_cliente=request.POST["txtcliente"]
    telefono=request.POST["txtedad"]
    guardarVenta=Clientes.objects.create(codigo=codigo, nombre=nombre,direccion=direccion,correo=correo, fecha=fecha, tipo_cliente=tipo_cliente, telefono=telefono)
    return redirect("Clientes")

def seleccionarCliente(request,codigo):
    clientes=Clientes.objects.get(codigo=codigo)
    return render(request, "editarClientes.html", {"misclientes": clientes})

def editarCliente(request):
    codigo=request.POST["txtcodigo"] 
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    correo=request.POST["txtcorreo"]
    fecha=request.POST["txtfecha"]
    tipo_cliente=request.POST["txtcliente"]
    telefono=request.POST["txtedad"]

    clientes=Clientes.objects.get(codigo=codigo)
    clientes.codigo=codigo
    clientes.nombre=nombre
    clientes.direccion=direccion
    clientes.correo=correo
    clientes.fecha=fecha
    clientes.tipo_cliente=tipo_cliente
    clientes.telefono=telefono
    clientes.save()
    return redirect("Clientes")

def borrarCliente(request, codigo):
    clientes=Clientes.objects.get(codigo=codigo)
    clientes.delete()

    return redirect("Clientes")