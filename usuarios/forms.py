from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado

class RegistroForm(UserCreationForm):
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    telefono = forms.CharField()
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = UsuarioPersonalizado
        fields = [
            'username',       # nombre de usuario
            'first_name',     # nombre real
            'last_name',      # apellido
            'email',
            'fecha_nacimiento',
            'telefono',
            'password1',
            'password2'
        ]