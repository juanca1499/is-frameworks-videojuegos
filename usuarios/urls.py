from django.urls import path
# Se importan las vistas a llamar en esta aplicación
# del proyecto 
from . import views

# Para que las urls puedan tener nombres parecidos 
# sin que haya mezcla de nombres
app_name = 'usuarios'

urlpatterns = [
    path('nuevo/',views.NuevoUsuario.as_view(), name='nuevo'),
    path('municipios/',views.obtiene_municipios, name='municipio'),
    # path('lista/', views.lista_categoria, name='lista'),
    # path('editar/<int:id>',views.editar_categoria,name='editar'),
    # path('eliminar/<int:id>', views.eliminar_categoria, name='eliminar'),
]

# eliminar/<int:id> Para indicar la recepción de un 
# argumento. Se indica el tipo de dato y el nombre.
