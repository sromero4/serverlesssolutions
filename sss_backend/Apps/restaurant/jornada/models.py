from django.db import models

from Apps.restaurant.usuario.models import Usuario

class Jornada(models.Model):
    jor_codigo = models.AutoField(primary_key=True)
    jor_iniciofechahora = models.DateTimeField()
    jor_finfechahora = models.DateTimeField(blank=True, null=True)
    jor_pedidototal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    jor_ventatotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    jor_fechacreacion = models.DateTimeField()
    usu_codigo = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usu_codigo')

    def __str__(self):
        return self.jor_codigo