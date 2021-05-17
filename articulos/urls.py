from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'articulos'

urlpatterns = [
    path(_('lista/'),views.lista,name='lista'),
    path(_('detalle/<int:pk>'),views.detalle,name='detalle'),
]