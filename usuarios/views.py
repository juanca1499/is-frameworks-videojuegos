from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.views import LoginView 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage 
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, AccessMixin
from django.contrib.auth.models import Group

from .token import token_activacion
from .models import Usuario, Municipio, Estado
from .forms import UsuarioForm, UsuarioRegistroForm

class NuevoUsuario(PermissionRequiredMixin,CreateView):
    model = Usuario
    form_class = UsuarioForm
    permission_required = 'usuarios.add_usuario'
    extra_context = {'etiqueta' : 'Nuevo',
    'boton' : 'Agregar',
    'us_nuevo' : True}                
    success_url = reverse_lazy('usuarios:lista')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        # Toma el dominio actual. Es muy util para produccion
        dominio = get_current_site(self.request)
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = token_activacion.make_token(user)
        # Le mandamos las variables requeridas en el formulario
        mensaje = render_to_string('confirmar_cuenta.html',
        {
            'usuario' : user,
            'dominio' : dominio,
            'uid' : uid,
            'token' : token
        }
        )
        asunto = 'Activar cuenta en el Sistema de Videojuegos'
        to = user.email
        # En el to se puede poner una lista de usuarios
        email = EmailMessage(
            asunto,
            mensaje,
            to=[to]
            )
        email.content_subtype = 'html'
        email.send()

        return super().form_valid(form)

class ActivarCuenta(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(kwargs['uid64'])
            token = kwargs['token']
            user = Usuario.objects.get(id=uid)
        except:
            user = None

        if user and token_activacion.check_token(user,token):
            user.is_active = True
            user.save()
            messages.success(self.request,'¡Cuenta activada con éxito!')
        else:
            messages.error(self.request,'Token inválido, contacta al administrador')
        
        return redirect('usuarios:login')


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

def obtiene_usuario_grupos(request):
    if request.method != 'GET':
        return JsonResponse({'error':'Petición incorrecta'}, safe=False, status=403)
    id_usuario = request.GET.get('id')
    grupos = Groups.objects.filter(user_id=id_usuario)
    json = []
    if not grupos:
        json.append({'error' : 'El usuario no tiene grupos asignados'})
    for grupo in grupos:
        json.append({'id_usuario' :id_usuario,
                     'id_grupo' :grupo})
    return JsonResponse(json, safe=False)

class UsuarioList(PermissionRequiredMixin,ListView):
    paginate_by = 5
    model = Usuario
    permission_required = 'usuarios.view_usuario'
    lista_grupos = Group.objects.all()

    extra_context = {'us_lista' : True,
                     'lista_grupos': lista_grupos}                
    template_name = 'usuarios:lista'

class UsuarioActualizar(PermissionRequiredMixin,UpdateView):
    model = Usuario
    permission_required = 'usuarios.change_usuario'
    form_class = UsuarioForm
    extra_context = {'etiqueta' : 'Actualizar',
                     'boton' : 'Guardar'}
    success_url = reverse_lazy('usuarios:lista')

class UsuarioEliminar(PermissionRequiredMixin,DeleteView):
    model = Usuario
    permission_required = 'usuarios.delete_usuario'
    success_url = reverse_lazy('usuarios:lista')

class UsuarioDetalle(PermissionRequiredMixin,DetailView):
    model = Usuario
    permission_required = 'usuarios.view_usuario'

class LoginUsuario(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

class SignUpUsuario(CreateView):
    model = Usuario
    template_name = 'signup.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('usuarios:login')        

def logout(request):
    auth.logout(request)
    return redirect('usuarios:login')

def modificar_usuario_grupo(request,pk):
    if request.method == "POST":
        usuario = Usuarios.objects.filter(id=pk)


    return redirect('usuario:lista')