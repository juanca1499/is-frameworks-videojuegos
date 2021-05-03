from django.db import models
from django.contrib.auth.models import User
from .validators import curp_validator, foto_validator
from django.utils.translation import gettext_lazy as _

class Usuario(User):
    curp = models.CharField(max_length = 18, validators = [curp_validator], blank=True, null=True)
    estado = models.ForeignKey("usuarios.Estado", verbose_name=_("Estado"), on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey("usuarios.Municipio", verbose_name=_("Municipio"), on_delete=models.CASCADE, blank=True, null=True)
    foto = models.ImageField(_("Foto de perfil"), upload_to='perfiles', blank=True, null=True, validators=[foto_validator])

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')

class Estado(models.Model):
    nombre = models.CharField(max_length = 50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _('Estado')
        verbose_name_plural = _('Estados')

class Municipio(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.ForeignKey("usuarios.Estado", verbose_name=_("Estado"), on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _('Municipio')
        verbose_name_plural = _('Municipios')