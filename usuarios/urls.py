from django.urls import path
# Se importan las vistas a llamar en esta aplicación
# del proyecto 
from . import views

# Para que las urls puedan tener nombres parecidos 
# sin que haya mezcla de nombres
app_name = 'usuarios'

urlpatterns = [
    path('lista/',views.UsuarioList.as_view(),name='lista'),
    path('nuevo/',views.NuevoUsuario.as_view(), name='nuevo'),
    path('editar/<int:pk>',views.UsuarioActualizar.as_view(),name='editar'),
    path('eliminar/<int:pk>',views.UsuarioEliminar.as_view(),name='eliminar'),
    path('ver/<int:pk>',views.UsuarioDetalle.as_view(),name='ver'),
    path('municipios/',views.obtiene_municipios, name='municipio'),
    path('login/',views.LoginUsuario.as_view(),name='login'),
    path('logout',views.logout,name='logout'),
    path('signup/',views.SignUpUsuario.as_view(),name='signup'),
    path('activar/<slug:uid64>/<slug:token>',views.ActivarCuenta.as_view(),name='activar'),
    path('usuario-grupos/',views.obtiene_usuario_grupos,name='usuario_grupos'),
    path('modificar-grupos/<int:pk>',views.modificar_usuario_grupo,name='modificar_usuario_grupo')
]

# eliminar/<int:id> Para indicar la recepción de un 
# argumento. Se indica el tipo de dato y el nombre.
