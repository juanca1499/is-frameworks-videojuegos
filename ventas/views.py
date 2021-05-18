from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from videojuego.models import VideoJuego
from .models import Venta, DetalleVenta

@login_required
def carrito(request):
    articulos = request.session['articulos'] 
    carrito_vacio = True
   
    if len(articulos) > 0:
        carrito_vacio = False
    
    if request.method == "POST":
        id = request.POST.get('id')
        cantidad = int(request.POST.get('cantidad'))
        precio = float(request.POST.get('precio'))
        videojuego = get_object_or_404(VideoJuego, id=id)
        # Ya se encuentran artículos añadidos al carrito de ese producto.
        if id in request.session['articulos']:
            request.session['articulos'][id] = request.session['articulos'][id] + cantidad
            request.session['total'] = request.session['total'] + cantidad * precio
        # Aún no se había agregado ese artículo al carrito.
        else:
            request.session['articulos'][id] = cantidad
            request.session['total'] = request.session['total'] + cantidad * precio

        if videojuego.cantidad > 0:
            videojuego.cantidad = videojuego.cantidad - cantidad
            videojuego.save()

    lista_articulos = []
    for id in articulos:
        videojuego = get_object_or_404(VideoJuego, id=id)
        lista_articulos.append(videojuego)
        
    extra_context = {'carrito_vacio' : carrito_vacio,
                     'articulos' : lista_articulos}
    return render(request,'carrito/lista.html',extra_context)

@login_required
def eliminar_item(request, id):
    articulo_liberado = request.session['articulos'][str(id)]
    total = request.session['total']
    videojuego = get_object_or_404(VideoJuego, id=id)
    videojuego.cantidad = videojuego.cantidad + articulo_liberado
    videojuego.save()
    id_eliminar = str(videojuego.id)
    del request.session['articulos'][id_eliminar]
    total = total - float(videojuego.precio * articulo_liberado)
    total = request.session['total'] = total
    return redirect('ventas:carrito')

@login_required
def comprar(request):
    if request.method == "POST":
        venta = Venta()
        usuario = get_object_or_404(User, username=request.user.username)
        venta.usuario = usuario
        venta.pagada = True
        venta.save()

        for id in request.session['articulos']:
            detalle_venta = DetalleVenta()
            videojuego = get_object_or_404(VideoJuego, id=id)
            cantidad = request.session['articulos'][id]
            detalle_venta.articulo = videojuego
            detalle_venta.cantidad = cantidad
            detalle_venta.precio = cantidad * videojuego.precio
            detalle_venta.venta = venta
            detalle_venta.save()
        request.session['articulos'] = {}
        request.session['total'] = 0.0
        return redirect('articulos:lista')  