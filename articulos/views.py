from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required

from videojuego.models import VideoJuego

@login_required
def lista(request):
    articulos = VideoJuego.objects.all()
    carrito_vacio = estado_carrito(request)
    extra_context = {'articulos' : articulos,
                     'carrito_vacio': carrito_vacio}
    return render(request,'lista.html', extra_context)

@login_required
def detalle(request,pk):
    articulo = VideoJuego.objects.get(id=pk)
    carrito_vacio = estado_carrito(request)
    extra_context = {'articulo' : articulo,
                     'carrito_vacio' : carrito_vacio}
    return render(request,'detalle.html', extra_context)

def estado_carrito(request):
    articulos = request.session['articulos']
    if len(articulos) > 0:
        return False
    else:
        return True
