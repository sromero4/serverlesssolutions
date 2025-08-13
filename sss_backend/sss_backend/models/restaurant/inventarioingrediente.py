from django.db import models


class Inventarioingrediente(models.Model):
    inving_codigo = models.AutoField(primary_key=True)
    inving_fechacreacion = models.DateTimeField()
    usu_codigo = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usu_codigo')
    inv_codigo = models.ForeignKey('Inventario', models.DO_NOTHING, db_column='inv_codigo')
    ing_codigo = models.ForeignKey('Ingrediente', models.DO_NOTHING, db_column='ing_codigo')

    class Meta:
        managed = False
        app_label = 'restaurant'
        db_table = 'inventarioingrediente'