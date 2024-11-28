from django.shortcuts import render, redirect
from .models import Categorias
# Create your views here.

def inicio_vistaCategorias(request):
    lasCategorias=Categorias.objects.all

    return render(request,"gestionarCat.html", {"miscategorias":lasCategorias})

def registrarCat(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    descripcion=request.POST["txtdescripcion"]
    fecha=request.POST["txtfecha"]
    activo=request.POST["txtactivo"]
    prioridad=request.POST["txtprioridad"]
    numc=request.POST["txtnumc"]
    guardarVenta=Categorias.objects.create(codigo=codigo,nombre=nombre ,descripcion=descripcion,  fecha=fecha, activo=activo,prioridad=prioridad,numc=numc)
    return redirect("Categoria")

def seleccionarCat(request,codigo):
    categorias=Categorias.objects.get(codigo=codigo)
    return render(request, "editarCat.html", {"miscategorias": categorias})

def editarCat(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    descripcion=request.POST["txtdescripcion"]
    fecha=request.POST["txtfecha"]
    activo=request.POST["txtactivo"]
    prioridad=request.POST["txtprioridad"]
    numc=request.POST["txtnumc"]
    
    categorias=Categorias.objects.get(codigo=codigo)
    categorias.codigo=codigo
    categorias.nombre=nombre
    categorias.descripcion=descripcion
    categorias.fecha=fecha
    categorias.activo=activo
    categorias.prioridad=prioridad
    categorias.fecha=fecha
    categorias.numc=numc
    categorias.save()
    return redirect("Categoria")

def borrarCat(request, codigo):
    categorias=Categorias.objects.get(codigo=codigo)
    categorias.delete()

    return redirect("Categoria")