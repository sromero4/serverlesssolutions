from django.db import models

from Apps.restaurant.usuario.models import Usuario

class Inventario(models.Model):
    inv_codigo = models.AutoField(primary_key=True)
    inv_fechahora = models.DateTimeField()
    usu_codigo = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usu_codigo')

    def __str__(self):
        return self.inv_codigo