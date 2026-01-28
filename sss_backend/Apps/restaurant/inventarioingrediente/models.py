from django.db import models

from Apps.restaurant.inventario.models import Inventario
from Apps.restaurant.ingrediente.models import Ingrediente
from Apps.restaurant.usuario.models import Usuario

class Inventarioingrediente(models.Model):
    inving_codigo = models.AutoField(primary_key=True)
    inving_fechacreacion = models.DateTimeField()
    usu_codigo = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usu_codigo')
    inv_codigo = models.ForeignKey('Inventario', models.DO_NOTHING, db_column='inv_codigo')
    ing_codigo = models.ForeignKey('Ingrediente', models.DO_NOTHING, db_column='ing_codigo')

    def __str__(self):
        return self.inving_codigo