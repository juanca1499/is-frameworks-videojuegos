from django.urls import path
# Se importan las vistas a llamar en esta aplicación
# del proyecto 
from . import views

# Para que las urls puedan tener nombres parecidos 
# sin que haya mezcla de nombres
app_name = 'videojuego'

urlpatterns = [
    # path('lista/',views.lista_vjuego,name='lista'),
    path('lista/',views.VideoJuegoList.as_view(),name='lista'),
    #path('nuevo/',views.nuevo_vjuego, name='nuevo'),
    path('nuevo/',views.VideoJuegoCrear.as_view(), name='nuevo'),
    path('editar/<int:pk>',views.VideoJuegoActualizar.as_view(),name='editar'),
    # path('eliminar/<int:id>',views.eliminar_vjuego,name='eliminar'),
    path('eliminar/<int:pk>',views.VideoJuegoEliminar.as_view(),name='eliminar'),
    path('ver/<int:pk>',views.VideoJuegoDetalle.as_view(),name='ver'),
    path('grafica/',views.Grafica.as_view(),name='grafica'),
]

# eliminar/<int:id> Para indicar la recepción de un 
# argumento. Se indica el tipo de dato y el nombre.
