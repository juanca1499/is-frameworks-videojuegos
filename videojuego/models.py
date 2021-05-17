from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import foto_validator

class VideoJuego(models.Model):
    titulo = models.CharField(_('Título'), max_length=50, unique=True)
    anio = models.IntegerField(_('Año'))
    categoria = models.ForeignKey("videojuego.Categoria",verbose_name=_('Categoría'),on_delete=models.CASCADE)
    precio = models.DecimalField(_('Precio'),max_digits=5, decimal_places=2)
    descripcion = models.CharField(_('Descripción'),max_length=250,
    null=True, blank=True)
    foto = models.ImageField(_("Foto"), upload_to='articulos', blank=True, null=True, validators=[foto_validator])

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = _('Videojuego')
        verbose_name_plural = _('Videojuegos')

class Categoria(models.Model):
    nombre = models.CharField(_('Categoría'),max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _('Categoría')
        verbose_name_plural = _('Categorías')
    
