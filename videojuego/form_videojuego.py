from django import forms
from .models import VideoJuego
from django.utils.translation import gettext as _

class VideoJuegoForm(forms.ModelForm):
    class Meta:
        model = VideoJuego
        fields = '__all__'

# Para personalizar más las vistas de los formularios
class VideoJuegoForm(forms.ModelForm):
    class Meta:
        model = VideoJuego
        fields = '__all__'
        widgets = {
            'titulo' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : _('Nombre del videojuego'),'onFocus' : 'validar(this)'}),
            'anio' : forms.NumberInput(attrs={'class' : 'form-control','placeholder' : _('Año de lanzamiento')}),
            'categoria' : forms.Select(attrs={'class' : 'form-control','placeholder' : _('Categoría')}),
            'precio' : forms.NumberInput(attrs={'class' : 'form-control','placeholder' : _('Precio US')}),
            'descripcion' : forms.Textarea(attrs={'class' : 'form-control','placeholder' : _('Descripción'),'rows' : 60})
        }