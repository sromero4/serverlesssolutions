from django.db import models


class Ingrediente(models.Model):
    ing_codigo = models.AutoField(primary_key=True)
    ing_nombre = models.CharField(max_length=100)
    ing_cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    ing_fechacreacion = models.DateTimeField()
    usu_codigo = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usu_codigo')
    tipprod_codigo = models.ForeignKey('Tipoproducto', models.DO_NOTHING, db_column='tipprod_codigo')
    tipcant_codigo = models.ForeignKey('Tipocantidad', models.DO_NOTHING, db_column='tipcant_codigo')

    class Meta:
        managed = False
        app_label = 'restaurant'
        db_table = 'ingrediente'