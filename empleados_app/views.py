from django.shortcuts import render, redirect
from .models import Empleados
# Create your views here.

def inicio_vistaEmpleados(request):
    losEmpleados=Empleados.objects.all

    return render(request,"gestionarEmp.html", {"misempleados":losEmpleados})

def registrarEmp(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    direccion=request.POST["txtdireccion"]
    puesto=request.POST["txtpuesto"]
    fecha=request.POST["txtfecha"]
    guardarVenta=Empleados.objects.create(codigo=codigo,nombre=nombre ,telefono=telefono,  correo=correo, direccion=direccion,puesto=puesto,fecha=fecha)
    return redirect("Empleados")

def seleccionarEmp(request,codigo):
    empleados=Empleados.objects.get(codigo=codigo)
    return render(request, "editarEmp.html", {"misempleados": empleados})

def editarEmp(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    direccion=request.POST["txtdireccion"]
    puesto=request.POST["txtpuesto"]
    fecha=request.POST["txtfecha"]
    
    empleados=Empleados.objects.get(codigo=codigo)
    empleados.codigo=codigo
    empleados.nombre=nombre
    empleados.telefono=telefono
    empleados.correo=correo
    empleados.direccion=direccion
    empleados.puesto=puesto
    empleados.fecha=fecha
    empleados.save()
    return redirect("Empleados")

def borrarEmp(request, codigo):
    empleados=Empleados.objects.get(codigo=codigo)
    empleados.delete()

    return redirect("Empleados")