from django.db import models


class Pedido(models.Model):
    ped_codigo = models.AutoField(primary_key=True)
    ped_mesa = models.CharField(max_length=20, blank=True, null=True)
    ped_tipo = models.CharField(max_length=50, blank=True, null=True)
    ped_horarecibido = models.TimeField(blank=True, null=True)
    ped_horaentrega = models.TimeField(blank=True, null=True)
    ped_subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ped_propina = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ped_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ped_adicional = models.TextField(blank=True, null=True)
    ped_metodopago = models.CharField(max_length=50, blank=True, null=True)
    ped_fechacreacion = models.DateTimeField()
    usu_codigo = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usu_codigo')
    jor_codigo = models.ForeignKey('Jornada', models.DO_NOTHING, db_column='jor_codigo')

    class Meta:
        managed = False
        app_label = 'restaurant'
        db_table = 'pedido'