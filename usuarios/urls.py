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
]

# eliminar/<int:id> Para indicar la recepción de un 
# argumento. Se indica el tipo de dato y el nombre.
