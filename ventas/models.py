from django.db import models
from django.utils.translation import gettext_lazy as _

class Venta(models.Model):
    usuario = models.ForeignKey("usuarios.Usuario", verbose_name=_("Usuario"), on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    pagada = models.BooleanField(_("Pagada"),default=False)

    class Meta:
        verbose_name = _('Venta')
        verbose_name_plural = _('Ventas')

class DetalleVenta(models.Model):
    articulo = models.ForeignKey("videojuego.Videojuego", verbose_name=_("Articulo"), on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(_("Cantidad"), default=1)
    precio = models.DecimalField(_("Precio"),max_digits=10, decimal_places=2)
    venta = models.ForeignKey("ventas.Venta",verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Detalle de Venta')
        verbose_name_plural = _('Detalles de Venta')