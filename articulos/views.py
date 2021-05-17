from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from videojuego.models import VideoJuego

def lista(request):
    articulos = VideoJuego.objects.all()
    extra_context = {'articulos' : articulos}
    return render(request,'lista.html', extra_context)

def detalle(request):
    return render(request,'detalle.html')