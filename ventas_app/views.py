from django.shortcuts import render, redirect
from .models import Ventas
# Create your views here.

def inicio_vistaVentas(request):
    lasVentas=Ventas.objects.all

    return render(request,"gestionarVentas.html", {"misventas":lasVentas})

def registrarVenta(request):
    codigo=request.POST["txtcodigo"] 
    id_cliente=request.POST["txtcliente"]
    fecha=request.POST["txtfecha"]
    total_venta=request.POST["txttotal"]
    id_producto=request.POST["txtmetodo"]
    id_empleado=request.POST["txtempleado"]
    estatus=request.POST["txtestatus"]
    guardarVenta=Ventas.objects.create(codigo=codigo, fecha=fecha,total_venta=total_venta, id_cliente=id_cliente, id_producto=id_producto, id_empleado=id_empleado, estatus=estatus)
    return redirect("Venta")

def seleccionarVenta(request,codigo):
    ventas=Ventas.objects.get(codigo=codigo)
    return render(request, "editarVentas.html", {"misventas": ventas})

def editarVentas(request):
    codigo=request.POST["txtcodigo"] 
    id_cliente=request.POST["txtcliente"]
    fecha=request.POST["txtfecha"]
    total_venta=request.POST["txttotal"]
    id_producto=request.POST["txtmetodo"]
    id_empleado=request.POST["txtempleado"]
    estatus=request.POST["txtestatus"]    
    ventas=Ventas.objects.get(codigo=codigo)
    ventas.codigo=codigo
    ventas.id_cliente=id_cliente
    ventas.fecha=fecha
    ventas.total_venta=total_venta
    ventas.id_producto=id_producto
    ventas.id_empleado=id_empleado
    ventas.estatus=estatus
    ventas.save()
    return redirect("Venta")

def borrarVenta(request, codigo):
    ventas=Ventas.objects.get(codigo=codigo)
    ventas.delete()

    return redirect("Venta")