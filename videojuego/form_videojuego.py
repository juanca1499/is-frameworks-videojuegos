from django import forms
from .models import VideoJuego

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
            'titulo' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Nombre del videojuego','onFocus' : 'validar(this)'}),
            'anio' : forms.NumberInput(attrs={'class' : 'form-control','placeholder' : 'Año de lanzamiento'}),
            'categoria' : forms.NumberInput(attrs={'class' : 'form-control','placeholder' : 'Categoría'}),
            'precio' : forms.NumberInput(attrs={'class' : 'form-control','placeholder' : 'Precio US'}),
            'descripcion' : forms.Textarea(attrs={'class' : 'form-control','placeholder' : 'Descripción'})
        }