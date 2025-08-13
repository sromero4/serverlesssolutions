from django.db import models


class Inventario(models.Model):
    inv_codigo = models.AutoField(primary_key=True)
    inv_fechahora = models.DateTimeField()
    usu_codigo = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usu_codigo')

    class Meta:
        managed = False
        app_label = 'restaurant'
        db_table = 'inventario'