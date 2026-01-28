from django.db import models
from Apps.restaurant.tipocantidad.models import Tipocantidad
from Apps.restaurant.tipoproducto.models import Tipoproducto
from Apps.restaurant.usuario.models import Usuario


class Ingrediente(models.Model):
    ing_codigo = models.AutoField(primary_key=True)
    ing_nombre = models.CharField(max_length=100)
    ing_cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    ing_fechacreacion = models.DateTimeField()
    usu_codigo = models.ForeignKey(Usuario, models.DO_NOTHING)
    tipprod_codigo = models.ForeignKey(Tipoproducto, models.DO_NOTHING)
    tipcant_codigo = models.ForeignKey(Tipocantidad, models.DO_NOTHING)

    def __str__(self):
        return self.ing_nombre