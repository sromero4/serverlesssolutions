from django.db import models

from Apps.restaurant.pedido.models import Pedido
from Apps.restaurant.producto.models import Producto

class Pedidoproducto(models.Model):
    pedprod_codigo = models.AutoField(primary_key=True)
    ped_codigo = models.ForeignKey(Pedido, models.DO_NOTHING)
    prod_codigo = models.ForeignKey(Producto, models.DO_NOTHING)

    def __str__(self):
        return self.pedprod_codigo