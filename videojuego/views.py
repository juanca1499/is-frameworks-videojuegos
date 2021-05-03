from django.shortcuts import render, redirect, get_object_or_404
# Se necesitan tener importadas las clases a usar.
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django_weasyprint import WeasyTemplateResponseMixin
from django.db.models import Count
from django.conf import settings
from django.core.paginator import Paginator
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy

from .models import Categoria, VideoJuego
from .form_categoria import CategoriaForm
from .form_videojuego import VideoJuegoForm
from .form_videojuego import VideoJuegoForm


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
    paginator = Paginator(categorias, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'lista_categorias.html',{'categorias' : categorias,
                                                    'cat_lista' : True,
                                                    'page_obj' : page_obj})

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
    paginate_by = 5
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
    extra_context = {'etiqueta' : gettext_lazy('Nuevo'),
    'boton' : gettext_lazy('Agregar'),
    'vj_nuevo' : True}
    # fields = '__all__'
    success_url = reverse_lazy('videojuego:lista')

class VideoJuegoActualizar(UpdateView):
    model = VideoJuego
    form_class = VideoJuegoForm
    extra_context = {'etiqueta' : gettext_lazy('Editar'),
    'boton' : gettext_lazy('Guardar')}
    success_url = reverse_lazy('videojuego:lista')

class VideoJuegoDetalle(DetailView):
    model = VideoJuego

class Grafica(TemplateView):
    template_name = 'videojuego/grafica.html'

    def get(self, request, *args, **kwargs):
        videojuegos_categoria = VideoJuego.objects.all().values('categoria').annotate(cuantos=Count('categoria'))
        categorias = Categoria.objects.all()
        datos = []
        for categoria in categorias:
            cuantos = 0
            for vj_categoria in videojuegos_categoria:
                if vj_categoria['categoria'] == categoria.id:
                    cuantos = vj_categoria['cuantos']
                    break
            datos.append({'name' : categoria.nombre,
                        'data' : [cuantos]})

        self.extra_context = {'datos' : datos}
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class VistaVideoJuegosPDF(ListView):
    model = VideoJuego
    template_name = 'videojuego/videojuegos_lista_pdf.html'

    def get(self, request, *args, **kwargs):
        suma = 0
        for videojuego in VideoJuego.objects.all():
            suma += videojuego.precio
        self.extra_context = {'suma' : suma}
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class ListaVideoJuegosPDF(WeasyTemplateResponseMixin,VistaVideoJuegosPDF):
    # output of MyModelView rendered as PDF with hardcoded CSS
    pdf_stylesheets = [
        settings.STATICFILES_DIRS[0] + 'css/bootstrap.min.css',
        settings.STATICFILES_DIRS[0] + 'css/estilo.css',
    ]
    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = False
    # custom response class to configure url-fetcher
    pdf_filename = 'ListaVideojuegos.pdf'

class VistaVideoJuegoDetallePDF(DetailView):
    model = VideoJuego
    template_name = 'videojuego/videojuego_detalle_pdf.html'

class VideoJuegoDetallePDF(WeasyTemplateResponseMixin, VistaVideoJuegoDetallePDF):
    # output of MyModelView rendered as PDF with hardcoded CSS
    pdf_stylesheets = [
        settings.STATICFILES_DIRS[0] + 'css/bootstrap.min.css',
        settings.STATICFILES_DIRS[0] + 'css/estilo.css',
    ]
    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = False
    # custom response class to configure url-fetcher
    pdf_filename = 'DetalleVideojuego.pdf'