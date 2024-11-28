from django.shortcuts import render, redirect
from .models import Productos
# Create your views here.

def inicio_vistaProductos(request):
    losProductos=Productos.objects.all

    return render(request,"gestionarProducto.html", {"misproductos":losProductos})

def registrarProducto(request):
    codigo=request.POST["txtcodigo"] 
    nombre=request.POST["txtnombre"]
    fecha=request.POST["txtfecha"]
    precio=request.POST["txtprecio"]
    descripcion=request.POST["txtdescripcion"]
    categoria=request.POST["txtcategoria"]
    stock=request.POST["txtstock"]
    guardarVenta=Productos.objects.create(codigo=codigo, nombre=nombre, fecha=fecha,precio=precio, descripcion=descripcion, categoria=categoria, stock=stock)
    return redirect("Producto")

def seleccionarProducto(request,codigo):
    productos=Productos.objects.get(codigo=codigo)
    return render(request, "editarProducto.html", {"misproductos": productos})

def editarProducto(request):
    codigo=request.POST["txtcodigo"] 
    nombre=request.POST["txtnombre"]
    fecha=request.POST["txtfecha"]
    precio=request.POST["txtprecio"]
    descripcion=request.POST["txtdescripcion"]
    categoria=request.POST["txtcategoria"]
    stock=request.POST["txtstock"]
    
    productos=Productos.objects.get(codigo=codigo)
    productos.codigo=codigo
    productos.nombre=nombre
    productos.precio=precio
    productos.fecha=fecha
    productos.descripcion=descripcion
    productos.categoria=categoria
    productos.stock=stock
    productos.save()
    return redirect("Producto")

def borrarProducto(request, codigo):
    productos=Productos.objects.get(codigo=codigo)
    productos.delete()

    return redirect("Producto")