from django import forms
from .models import Categoria
from django.utils.translation import gettext as _

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
    
        widgets = {
            'nombre' : forms.TextInput(attrs={'class' : 'form-control',
                                              'placeholder' : _('Nombre de la categoría')})
        }
    

