from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Usuario, Municipio, Estado
from .forms import UsuarioForm
from django.http import JsonResponse

class NuevoUsuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    extra_context = {'etiqueta' : 'Nuevo',
    'boton' : 'Agregar',
    'us_nuevo' : True}                
    success_url = reverse_lazy('usuarios:lista')

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)

def obtiene_municipios(request):
    # estado = get_object_or_404(Estado, id=id_estado)
    if request.method == 'GET':
        return JsonResponse({'error':'Petición incorrecta'}, safe=False, status=403)
    id_estado = request.POST.get('id')
    municipios = Municipio.objects.filter(estado_id=id_estado)
    json = []
    if not municipios:
        json.append({'error' : 'No se encontraron municipios con ese estado'})
    for municipio in municipios:
        json.append({'id' : municipio.id,
                     'nombre' : municipio.nombre})
    return JsonResponse(json, safe=False)

class UsuarioList(ListView):
    model = Usuario
    extra_context = {'us_lista' : True}                
    template_name = 'usuarios:lista'

class UsuarioActualizar(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    extra_context = {'etiqueta' : 'Actualizar',
                     'boton' : 'Guardar'}
    success_url = reverse_lazy('usuarios:lista')

class UsuarioEliminar(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuarios:lista')

class UsuarioDetalle(DetailView):
    model = Usuario
