from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'ventas'

urlpatterns = [
    path(_('carrito'), views.carrito, name='carrito'),
    path(_('eliminar-item/<int:id>'), views.eliminar_item, name='eliminar_item_carrito'),
    path(_('comprar'), views.comprar, name='comprar')
]