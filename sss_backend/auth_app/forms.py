from django import forms

class IngredienteForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre del ingrediente",
        max_length=100,
        required=True
    )
    cantidad = forms.DecimalField(
        label="Cantidad",
        min_value=0.01,
        decimal_places=2,
        required=True
    )
    tipo_producto = forms.IntegerField(
        required=False,
        initial=1
    )
    tipo_cantidad = forms.IntegerField(
        required=False,
        initial=1
    )
