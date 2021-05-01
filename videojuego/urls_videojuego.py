from django.urls import path
# Se importan las vistas a llamar en esta aplicación
# del proyecto 
from . import views
from django.views.i18n import JavaScriptCatalog
from django.utils.translation import gettext_lazy as _

# Para que las urls puedan tener nombres parecidos 
# sin que haya mezcla de nombres
app_name = 'videojuego'

urlpatterns = [
    # path('lista/',views.lista_vjuego,name='lista'),
    path(_('lista/'),views.VideoJuegoList.as_view(),name='lista'),
    #path('nuevo/',views.nuevo_vjuego, name='nuevo'),
    path(_('nuevo/'),views.VideoJuegoCrear.as_view(), name='nuevo'),
    path(_('editar/<int:pk>'),views.VideoJuegoActualizar.as_view(),name='editar'),
    # path('eliminar/<int:id>',views.eliminar_vjuego,name='eliminar'),
    path(_('eliminar/<int:pk>'),views.VideoJuegoEliminar.as_view(),name='eliminar'),
    path(_('ver/<int:pk>'),views.VideoJuegoDetalle.as_view(),name='ver'),
    path(_('grafica/'),views.Grafica.as_view(),name='grafica'),
    path(_('pdf-lista/'),views.ListaVideoJuegosPDF.as_view(), name='lista_pdf'),
    path(_('pdf-detalle/<int:pk>'),views.VideoJuegoDetallePDF.as_view(),name='detalle_pdf'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript_catalog'),
]

# eliminar/<int:id> Para indicar la recepción de un 
# argumento. Se indica el tipo de dato y el nombre.
