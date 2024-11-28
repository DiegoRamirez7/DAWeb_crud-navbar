from django.shortcuts import render, redirect
from .models import Proveedores
# Create your views here.

def inicio_vistaProveedores(request):
    losProveedores=Proveedores.objects.all

    return render(request,"gestionarPro.html", {"misproveedores":losProveedores})

def registrarPro(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    direccion=request.POST["txtdireccion"]
    principal=request.POST["txtprincipal"]
    guardarVenta=Proveedores.objects.create(codigo=codigo,nombre=nombre ,telefono=telefono,  correo=correo, direccion=direccion,principal=principal)
    return redirect("Proveedores")

def seleccionarPro(request,codigo):
    proveedores=Proveedores.objects.get(codigo=codigo)
    return render(request, "editarPro.html", {"misproveedores": proveedores})

def editarPro(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    direccion=request.POST["txtdireccion"]
    principal=request.POST["txtprincipal"]
    
    proveedores=Proveedores.objects.get(codigo=codigo)
    proveedores.codigo=codigo
    proveedores.nombre=nombre
    proveedores.telefono=telefono
    proveedores.correo=correo
    proveedores.direccion=direccion
    proveedores.principal=principal
    proveedores.save()
    return redirect("Proveedores")

def borrarPro(request, codigo):
    proveedores=Proveedores.objects.get(codigo=codigo)
    proveedores.delete()

    return redirect("Proveedores")