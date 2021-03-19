from django import forms 
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ('username','password','first_name','last_name','estado','municipio','foto')

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control',
                                                'placeholder' : 'Crea un nombre de usuario'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 
                                                   'placeholder':'Crea una contraseña'}), 
            'first_name' : forms.TextInput(attrs={'class' : 'form-control',
                                                    'placeholder' : 'Indica tu nombre'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control',
                                                 'placeholder' : 'Indica tus apellidos'}),                                                    
            'estado' : forms.Select(attrs={'class':'form-control'}),
            'municipio' : forms.Select(attrs={'class':'form-control'}),
        }

    # Para guardar la contraseña de forma segura.
    def save(self, commit=True):
        user = super(UsuarioForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    