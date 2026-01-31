from .models import *
from django import forms


class CrearIngredienteForm(forms.ModelForm):

    class Meta:
        model = Ingrediente
        fields = (
            'ing_nombre',
            'ing_cantidad',
            'tipprod_codigo',
            'tipcant_codigo',
        )