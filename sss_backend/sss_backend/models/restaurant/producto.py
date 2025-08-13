from django.db import models


class Producto(models.Model):
    prod_codigo = models.AutoField(primary_key=True)
    prod_nombre = models.CharField(max_length=100)
    prod_descripcion = models.TextField(blank=True, null=True)
    prod_precio = models.DecimalField(max_digits=10, decimal_places=2)
    prod_imagen = models.CharField(max_length=255, blank=True, null=True)
    prod_fechacreacion = models.DateTimeField()
    prod_fechamodificacion = models.DateTimeField(blank=True, null=True)
    est_codigo = models.ForeignKey('Estado', models.DO_NOTHING, db_column='est_codigo')
    usu_codigo = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usu_codigo')

    class Meta:
        managed = False
        app_label = 'restaurant'
        db_table = 'producto'