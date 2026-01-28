from django.db import models


class Gasto(models.Model):
    gas_codigo = models.AutoField(primary_key=True)
    gas_fechacompra = models.DateTimeField()
    gas_monto = models.DecimalField(max_digits=10, decimal_places=2)
    gas_descripcion = models.TextField(blank=True, null=True)
    gas_observaciones = models.TextField(blank=True, null=True)
    gas_imagen = models.CharField(max_length=255, blank=True, null=True)
    gas_fechacreacion = models.DateTimeField()

    def __str__(self):
        return self.gas_codigo