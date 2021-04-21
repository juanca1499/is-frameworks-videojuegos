from django import forms 
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ('username','password','email','first_name','last_name','curp','estado','municipio','foto')

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control',
                                                'placeholder' : 'Crea un nombre de usuario'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control',
                                                   'placeholder' : 'Crea una contraseña'}), 
            'email' : forms.EmailInput(attrs={'class' : 'form-control',
                                             'placeholder' : 'Indica tu correo electrónico'}), 
            'first_name' : forms.TextInput(attrs={'class' : 'form-control',
                                                    'placeholder' : 'Indica tu nombre'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control',
                                                 'placeholder' : 'Indica tus apellidos'}),  
            'curp' : forms.TextInput(attrs={'class' : 'form-control',
                                            'placeholder' : 'Indica tu CURP'}),                                                                                              
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

class UsuarioRegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username','password')