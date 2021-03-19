from django.shortcuts import render, redirect, get_object_or_404
# Se necesitan tener importadas las clases a usar.
from .models import Categoria, VideoJuego
from .form_categoria import CategoriaForm
from .form_videojuego import VideoJuegoForm
from .form_videojuego import VideoJuegoForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

#################################
## VISTAS BASADAS EN FUNCIONES ##
#################################

def nuevo_categoria(request):
    form = CategoriaForm()

    # Este camino se toma cuando se envía algo desde el 
    # front-end hacia al back-end.
    # En nuestro caso se envía el nombre de la categoría
    # y se valida el dato para guardarlo en la DB.
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista')
        
    context = {'form' : form,
                'cat_nuevo' : True }
    return render(request,'nuevo_categoria.html',context)

def lista_categoria(request):
    # Se necesitan recuperar los objetos tipo Categoria.
    categorias = Categoria.objects.all()
    return render(request,'lista_categorias.html',{'categorias' : categorias,
                                                    'cat_lista' : True})

def editar_categoria(request,id):
    categoria = get_object_or_404(Categoria,id=id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista')

    form = CategoriaForm(instance=categoria)
    context = {'form' : form }
    return render(request,'editar_categoria.html',context)

def eliminar_categoria(request,id):
    # Para obtener el objeto o un 404 en caso de que no exista.
    categoria = get_object_or_404(Categoria,id=id)
    categoria.delete()
    return redirect('categoria:lista')

def nuevo_vjuego(request):
    form = VideoJuegoForm()
    if request.method == 'POST':
        form = VideoJuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('videojuego:lista')
    context = {'form' : form}
    return render(request,'nuevo_videojuego.html',context)

def lista_vjuego(request):
    videojuegos = VideoJuego.objects.all()
    return render(request,'lista_videojuegos.html',{'videojuegos' : videojuegos})

def editar_vjuego(request,id):
    videojuego = VideoJuego.objects.get(id=id)

    if request.method == 'POST':
        form = VideoJuegoForm(request.POST,instance=videojuego)
        if form.is_valid():
            form.save()
            return redirect('videojuego:lista')
    form = VideoJuegoForm(instance=videojuego)
    context = {'form' : form}
    return render(request,'editar_videojuego.html',context)

def eliminar_vjuego(request,id):
    videojuego = VideoJuego.objects.get(id=id)
    videojuego.delete()
    return redirect('videojuego:lista')

# ------------------------------------------------------------- #

# -------------------------------------------------------------- #

##############################
## VISTAS BASADAS EN CLASES ##
#############################

class VideoJuegoList(ListView):
    model = VideoJuego
    template_name = 'videojuego:lista'
    extra_context = {'vj_lista' : True}
        # Para cambiar el nombre de la instancia #
    # context_object_name = 'videojuegos'
        # Para enviar información extra #
    # extra_context =  {
    #     'var1' : 'Clases Genéricas',
    #     'nombre' : 'Juan Carlos',
    # }
        # Para hacer un filtro #
    # querset = VideoJuego.objects.filter(precio=0)

class VideoJuegoEliminar(DeleteView):
    model = VideoJuego
    success_url = reverse_lazy('videojuego:lista')

class VideoJuegoCrear(CreateView):
    model = VideoJuego
    form_class = VideoJuegoForm
    extra_context = {'etiqueta' : 'Nuevo',
    'boton' : 'Agregar',
    'vj_nuevo' : True}
    # fields = '__all__'
    success_url = reverse_lazy('videojuego:lista')

class VideoJuegoActualizar(UpdateView):
    model = VideoJuego
    form_class = VideoJuegoForm
    extra_context = {'etiqueta' : 'Actualizar',
    'boton' : 'Guardar'}
    success_url = reverse_lazy('videojuego:lista')

class VideoJuegoDetalle(DetailView):
    model = VideoJuego
