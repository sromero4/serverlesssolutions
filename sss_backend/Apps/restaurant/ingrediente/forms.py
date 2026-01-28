from .models import *
from django import forms


class CrearIngredienteForm(forms.ModelForm):

    class Meta:
        model = Ingrediente
        fields = (
            'nombre',
            'cantidad',
            'fechacreacion',
            'usuario',
            'tipoproducto',
            'tipocantidad',
        )