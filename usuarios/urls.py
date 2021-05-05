from django.urls import path
# Se importan las vistas a llamar en esta aplicación
# del proyecto 
from . import views
from django.utils.translation import gettext_lazy as _

# Para que las urls puedan tener nombres parecidos 
# sin que haya mezcla de nombres
app_name = 'usuarios'

urlpatterns = [
    path(_('lista/'),views.UsuarioList.as_view(),name='lista'),
    path(_('nuevo/'),views.NuevoUsuario.as_view(), name='nuevo'),
    path(_('editar/<int:pk>'),views.UsuarioActualizar.as_view(),name='editar'),
    path(_('eliminar/<int:pk>'),views.UsuarioEliminar.as_view(),name='eliminar'),
    path(_('ver/<int:pk>'),views.UsuarioDetalle.as_view(),name='ver'),
    path(_('municipios/'),views.obtiene_municipios, name='municipio'),
    path(_('login/'),views.LoginUsuario.as_view(),name='login'),
    path(_('logout/'),views.logout,name='logout'),
    path(_('signup/'),views.SignUpUsuario.as_view(),name='signup'),
    path(_('activar/<slug:uid64>/<slug:token>'),views.ActivarCuenta.as_view(),name='activar'),
    path(_('modificar-grupos/<int:id>'),views.modificar_usuario_grupo,name='modificar_usuario_grupo'),
]

# eliminar/<int:id> Para indicar la recepción de un 
# argumento. Se indica el tipo de dato y el nombre.
