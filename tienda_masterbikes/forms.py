from django import forms
from .models import Arriendo


class ArriendoForm(forms.ModelForm):
    class Meta:
        model = Arriendo
        fields = ['bicicleta', 'fecha', 'hora_inicio', 'hora_fin']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time'}),
        }