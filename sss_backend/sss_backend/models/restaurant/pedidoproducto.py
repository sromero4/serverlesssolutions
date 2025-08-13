from django.db import models


class Pedidoproducto(models.Model):
    pedprod_codigo = models.AutoField(primary_key=True)
    ped_codigo = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='ped_codigo')
    prod_codigo = models.ForeignKey('Producto', models.DO_NOTHING, db_column='prod_codigo')

    class Meta:
        managed = False
        app_label = 'restaurant'
        db_table = 'pedidoproducto'